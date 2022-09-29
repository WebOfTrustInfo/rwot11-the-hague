from verifiable_credentials import issue

batch = issue.BlockcertsBatch(
    issuer=issuer,
     assertion=assertion,
     recipients=recipients,
     anchor_handler=eth_anchor_handler,
)
tx_id, final_certs = batch.run()
