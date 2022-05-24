# Sharing Personal Health Data to Improve Treatment of Chronic Conditions
Benay Dara-Abrams, PhD, CTO, [BrainJolt](http://brainjolt.com), benay@dara-abrams.com
## Problem
In the U.S. today, more than 40% of adults are suffering from two or more chronic medical conditions. 
Primary care practices are treating an increasing number of patients with multiple chronic conditions as 
the aging population continues to grow. This results in spending 71% of U.S. health care dollars on 
managing chronic conditions. While patients can appreciate the importance of managing their chronic 
conditions, they may be overwhelmed by the challenges of adhering to a complex medication regimen 
while trying to stick to good health habits like exercising and eating a healthy diet.

## Monitoring Chronic Conditions
To improve monitoring and self-management of chronic conditions, patient-reported outcomes (PROs) 
can be recorded in real time between office visits. This information provides a more complete and 
accurate view of the patient¿s current health status than self-reports based on patient recall during an 
office visit. With a better understanding of the patient¿s current health situation, PROs help patients work 
with their physicians to monitor and better manage their chronic conditions.

## Open mHealth and IEEE P1752 Standard for Mobile Health Data
Believing that no single app or device provides all the information for an individual¿s health story, Open 
mHealth is focused on making patient-generated data from disparate sources accessible, providing an 
interoperability standard for harmonizing and helping make sense of digital health data. A working 
group is currently developing the IEEE P1752 Standard for Mobile Health Data, with the scope and 
purpose described below. (Note: I recently joined the working group).
> Scope:  This standard will define specifications for a mobile health data applications programming 
interface (API) and standardized representations for mobile health data and metadata. Mobile health data 
encompasses personal health data collected from sensors and mobile applications.

> Purpose: The purpose is to provide standard semantics to enable meaningful description, exchange, 
sharing, and use of mobile health data. Data and associated metadata will be sufficiently clear and 
complete to support analysis for a set of consumer health, biomedical research, and clinical care needs.

## Protecting Personal Health Data
Since each person¿s health story includes data from different sources, each source of data needs to be 
identified as pertaining to a particular individual while protecting the individual¿s Personal Information (PI), 
Personally Identifiable Information (PII), and Protected Heath Information (PHI).
Privacy standards and guidelines mentioned by the IEEE P1752 working group include:

*	HL7 FHIR (Fast Healthcare Interoperability Resources) Release 4 is a standard for 
exchanging healthcare information electronically. The standard includes a Security & Privacy 
module, which describes access control and authorization to protect a FHIR server, consent 
documenting the permissions a user has granted, and provenance and audit logging to record 
events that have been performed. While the FHIR specification provides a set of building blocks
to create secure, private systems, it doesn't specify any particular technical approach to security and privacy.

*	The IEEE P7002 Data Privacy Process standard defines requirements for a systems/software 
engineering process for privacy oriented considerations for organizations and projects developing 
and deploying products, systems, processes, and applications involving personal information. 

*	The National Institute of Standards and Technology (NIST) Privacy Framework helps 
organizations manage privacy risks from Personally Identifiable Information (PII) about individuals 
being collected, stored, used, and shared by an organization during the use of the organization¿s 
products and services.

*	Xcertia mHealth App Privacy Guidelines assess whether a mobile health app protects the 
user¿s information, including Protected Health Information (PHI), Personal Information (PI), and 
Personally Identifiable Information (PII) in full compliance with all applicable laws, rules and 
regulations.

## Protecting Personal Health Data with Decentralized Digital Identity
I would like to work with others to develop scenarios demonstrating how decentralized digital identity can 
help in protecting Personally Identifiable Information (PII), Personal Information (PI), and Protected Health 
Information (PHI) while facilitating sharing of personal health data in the context of Open mHealth and the 
IEEE P1752 Standard for Mobile Health Data.

## References
* HL7 FHIR Release 4 https://www.hl7.org/fhir/overview.html
* HL7 FHIR Security and Privacy Module https://www.hl7.org/fhir/secpriv-module.html
* IEEE P1752 Working Group https://site.ieee.org/sagroups-1752/
* IEEE P7002 Data Privacy Process https://standards.ieee.org/project/7002.html#Standard
* Improving the Management of Multiple Chronic Conditions with mPROVE https://digital.ahrq.gov/ahrq-funded-project/improving-management-multiple-chronic-conditions-mprove
* Mobile Devices and Health, Ida Sim, The New England Journal of Medicine, Sept. 5, 2019 
https://www.nejm.org/doi/full/10.1056/NEJMra1806949
* NIST Privacy Framework: An Enterprise Risk Management Tool 
https://www.federalregister.gov/documents/2018/11/14/2018-24714/developing-a-privacy-framework
* Online Psychosocial Assessment Instruments NIH / National Institute on Aging STTR Grant Number: 
1R41AG037216-01 Final Report. http://brainjolt.com/reports/1R41AG037216-01_NIA-STTR-Final.pdf
* Open mHealth https://www.openmhealth.org/
* Sensor-Enabled Elder Social Support Platform NIH / National Institute on Aging STTR Grant Number: 
1R41AG035452-01 Final Report http://brainjolt.com/reports/1R41AG035452-01_NIH-NIA-STTR-Final_Report.pdf
* Toward a Model for Collaborative Gerontechnology: Connecting Elders and their Caregivers. 
http://brainjolt.com/reports/collabgerontech_forBJ_site_Aug2017.pdf
* Use of Mobile Devices to Measure Outcomes in Clinical Research, 2010-2016: A Systematic Literature 
Review https://www.karger.com/Article/Fulltext/486347
* XCertia mHealth App Guidelines https://xcertia.org/wp-content/uploads/2019/08/xcertia-guidelines-2019-final.pdf


