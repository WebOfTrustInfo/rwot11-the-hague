# Why Matrix Parameters?

By [Markus Sabadello](https://danubetech.com/) (<markus@danubetech.com>)

## 1. Introduction

The `did-url` ABNF grammar in the DID Core specification [1] currently looks like this:

```
did-url = did *( ";" param ) path-abempty [ "?" query ][ "#" fragment ]
```

Besides the DID itself, this also has a number of familiar syntax components that we
also have in HTTP(S) URLs, such as path, query string, and fragment. But hey, what's this
additional rule `param`? This is a construct called matrix parameter, which was first
considered as a syntax component for URIs over 20 years ago [2]. It is a way of passing
parameters as part of a DID URL. But wait, can't we already do that with query parameters,
why would we need this additional pattern?

## 2. How we mostly use DIDs and DID documents

For many applications in the DID community, only DIDs themselves are needed, there is often no
need for constructing DID URLs beyond that, and often DID documents are very simple. For example,
for simple DID-Auth login applications, only a DID and a simple DID document with
only a public key is required:

`did:ex:123`

```
{
  "@context": "https://www.w3.org/ns/did/v1",
  "id": "did:ex:123",
  "authentication": [{
    "id": "did:ex:123#keys-1",
    "type": "Ed25519VerificationKey2018",
    "publicKeyBase58": "H3C2AVvLMv6gmMNam3uVAjZpfkcJCwDwnZn6z3wXmqPV"
  }]
}
```

For many other DID applications, such as the DIDComm agent-to-agent protocol, DID URLs beyond
plain DIDs may not be needed either, and only a service endpoint is added to the public key in the
DID document:

`did:ex:123`

```
{
  "@context": "https://www.w3.org/ns/did/v1",
  "id": "did:ex:123",
  "authentication": [{
    "id": "did:ex:123#keys-1",
    "type": "Ed25519VerificationKey2018",
    "publicKeyBase58": "H3C2AVvLMv6gmMNam3uVAjZpfkcJCwDwnZn6z3wXmqPV"
  }],
  "service": [{
    "id": "did:ex:123",
    "type": "AgentService",
    "serviceEndpoint": "https://agency.com/myagent"
  }]
}
```

The above is sufficient for 90% (or more?) of the DID-based use cases; this influences our thinking,
and DID URLs or DID documents that are different from the above are sometimes quickly dismissed as
"too complex".

## 3. Service/link discovery

But DID documents can contain more than just a single public key and/or service endpoint. A DID
document could contain many services/links associated with my DID, and not all of them necessarily
require a special protocol or DID-based authentication or encryption. I may just as well use my
DID document to publicly announce my website or blog or other URLs that others can use to interact
with me. I want others to be able to discover such services or links from my DID:

`did:ex:123`

```
{
  "@context": "https://www.w3.org/ns/did/v1",
  "id": "did:ex:123",
  "service": [{
    "id": "did:ex:123#homepage",
    "serviceEndpoint": "https://alice.me/home/"
  }, {
    "id": "did:ex:123#work",
    "serviceEndpoint": "https://acmecorp.com/employees/alice-7332"
  }, {
    "id": "did:ex:123#linkedin",
    "type": "SocialNetworkService",
    "serviceEndpoint": "https://www.linkedin.com/in/alice-b26187c4/"
  }, {
    "id": "did:ex:123#message",
    "type": "ActivityPubService",
    "serviceEndpoint": "https://chaos.social/@alice01"
  }, {
    "id": "did:ex:123#files",
    "serviceEndpoint": "https://filestore.org/user123/"
  }
}
```

The idea of discovering links associated with an identifier is not a new invention with DIDs, there
have been other mechanisms before, such as `<link>` HTML elements:

```
GET https://alice.me/ HTTP/1.1

....
<link rel="stylesheet" href="/media/example.css">
....
```

In the IndieWeb community [3], this has been used not only to discover technical information related
to a website (e.g. stylesheets), but also to discover links to additional services of individuals:

```
<link rel="micropub" href="https://alice.me/pub">
<link rel="profile" href="https://profiles.com/alice">
```

Or using the `Link` HTTP header instead of a `<link>` HTML element:

```
Link: <https://profiles.com/alice>; rel="profile"
```

Being able to discover services/links from a URL is one of the fundamental features of Web
architecture itself, as Ivan Herman points out in his topic paper "DID and the Web" [4].

## 4. Persistent URLs (PURLs)

Before continuing with service/link discovery, let's take a quick detour to look at 
Persistent URLs (PURLs).

From Wikipedia [5] :

_“A Persistent URL is an address on the World Wide Web that causes a redirection to another Web resource. If a Web resource changes location (and hence URL), a PURL pointing to it can be updated.”_

Today: `http://purl.org/some/path` → `http://example.com/another/path`

Tomorrow: `http://purl.org/some/path` → `http://selfhosted.me:8080/`

_“The PURL service includes a concept known as partial redirection.”_

`http://purl.org/some/path/and/some/more/data` → `http://example.com/another/path/and/some/more/data`

Note how the part **/and/some/more/data** is included in the redirection process.

_“The concept of partial redirection allows hierarchies of Web-based resources to be addressed via PURLs without each resource requiring its own PURL.”_

So wait, persistent URLs? Aren't DIDs also persistent identifiers? Yes, and they are persistent not by convention or contractual relationships (as is the case with PURLs), they are persistent due to their cryptographic and decentralized properties. So can we use DIDs as a basis for PURLs, instead of HTTP(S) URLs?

## 5. DIDs as persistent URLs

One difference is that the above PURLs only redirect to a single URL, whereas DIDs and DID documents allow discovery of multiple services/links associated with a DID (e.g. website, personal blog, LinkedIn page, ActivityPub endpoint, file service, etc.). So if we want to construct a persistent URL based on DIDs, we need a way to select which service/link in the DID document we want to redirect to.

We could use a query parameter, or maybe a fragment, to indicate in a DID URL which service/link we want, e.g. we could do:

`did:ex:123?service=files`

`did:ex:123#files`

... in order to select this service from the DID document:

```
{
  "@context": "https://www.w3.org/ns/did/v1",
  "id": "did:ex:123",
  "service": [{
    "id": "did:ex:123#files",
    "serviceEndpoint": "https://filestore.org/user123/"
  }
}
```

But wait, in PURLs, didn't we have a feature called _partial redirection_? This means that I can have
additional syntax components such as path, query string, and fragment in my persistent URL, and it
would be automatically applied to the redirected URL, e.g. I should be able to have a persistent DID URL that
works like this:

Today: `did:ex:123/myresume/doc` → `https://filestore.org/user123/myresume/doc`

Tomorrow: `did:ex:123/myresume/doc` → `https://selfhosted.me:8080/myresume/doc`

Note how the part **/myresume/doc** is included in the redirection process.

Oh no, but now I forgot to indicate in my DID URL which service/link I wanted to redirect to in
my DID document (the `#files` one). So maybe I can add that back in as a query string
(`did:ex:123?service=files`)? Or as a fragment (`did:ex:123#files`)?

But what if in my DID URL itself I also want
to have a query string and/or a fragment, to be used not for service/link selection in the
DID document, but for the _partial redirection_ process, i.e. I want to have a path, query string, and
fragment in my DID URL that will all be included in the redirection:

`did:ex:123/myresume/doc?version=latest#intro` →

`https://filestore.org/user123/myresume/doc?version=latest#intro`

Now I can't add the `#files` identifier for the service/link anywhere, because I'm already using
all syntax components for identifying a Web resource. This is why an additional mechanism for passing parameters was added to DID URL syntax: Matrix parameters. Example:

`did:ex:123;service=files/myresume/doc?version=latest#intro`

## 6. Why matrix parameters?

In the above example, matrix parameters are used to influence the DID resolution process (in this
case, to select a service/link from the DID document), whereas the other syntax components path,
query string, and fragment are used "in the traditional way" to identify a resource under the authority of the DID. There
is no conflict between the two "layers" of DID URL dereferencing.

This allows us to combine the best features of service/link discovery (section 3) and persistent
URLs (section 4), AND we get all the features of DIDs themselves, such as decentralization and
cryptographic verifiability.

This enables not only self-sovereign identifiers for applications such as DID Auth or DIDComm agents,
but it also enables persistent, self-sovereign URLs for identifying any arbitrary resource on the web. In
order to not interfere with that, the core DID specification must not define any special uses of the traditional
syntax components path, query string, and fragment, in the same way as the HTTP(S) specification
does not define special uses of path, query string, and fragment.

## 7. Other matrix parameters

After realizing that we wanted separate syntax for 1. passing parameters to the resources identified by a DID URL (query parameters), and 2. passing parameters to the DID resolution process itself (matrix parameters), we discovered that there are more use cases than just service/link selection.

The matrix parameters `version-id` and `version-time` indicate that not the latest DID document should be
used during the DID resolution process, but an earlier version of the DID document. Again, we felt
that it would be problematic to use query parameters for this, since they may already be used for
a resource identified by the DID URL, not for influencing the DID resolution process. You could 
even construct a DID URL that indicates a version of the DID document, and separately the version
of a Web resource:

```
did:ex:123;service=files;version-id=4/myresume/doc?version=7#intro
```

Or to borrow a construct from Crytographic Hyperlinks [6], a DID URL could separately include a
resource hash for the DID document (a `hl` matrix parameter) and a resource hash for the Web resource
identified by the DID URL (a `hl` query parameter):

```
did:ex:123;service=files;hl=zQmWvQ/myresume/doc?hl=zQrMLp#intro
```

Yet another useful matrix parameter is `initial-values`, which can include a hint for the DID resolution
process to be able to obtain the DID document that may not have been fully created or anchored yet
by a DID method [7].

## 8. Conclusion

Let's not be scared by the fact that matrix parameters are an old proposal that never saw
broad adoption on the Web so far. Let's instead consider the use cases, let's consider how
DIDs fit in with Web architecture, and let's discuss the pros and cons of this syntax.

## 9. See also

This content is also available in a more readable slide form at [https://github.com/w3c-ccg/meetings/tree/gh-pages/2020-01-16-did-resolution](https://github.com/w3c-ccg/meetings/tree/gh-pages/2020-01-16-did-resolution).

For the initial discussion in the W3C Credentials Community Group [8] that eventually led to matrix parameters in DID URLs, see [https://github.com/w3c-ccg/did-spec/issues/90](https://github.com/w3c-ccg/did-spec/issues/90).

## References

[1] https://w3c.github.io/did-core/

[2] https://www.w3.org/DesignIssues/MatrixURIs.html

[3] https://indieweb.org/rel-values

[4] https://github.com/WebOfTrustInfo/rwot10-buenosaires/blob/master/topics-and-advance-readings/DID_and_the_Web.md

[5] https://en.wikipedia.org/wiki/Persistent_uniform_resource_locator

[6] https://tools.ietf.org/html/draft-sporny-hashlink-02

[7] https://github.com/w3c/did-core/pull/84

[8] https://www.w3.org/community/credentials/
