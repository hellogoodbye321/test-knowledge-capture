Project Deep Dive: The 'Hooli' & 'Phoenix' Chronicles
This repository contains simulated enterprise data representing a high-stakes transition period. To understand how the AI performs Knowledge Mining, you must understand the two primary technical threads running through the data:

1. The Hooli Corp Acquisition (The Business Baseline)
The Context: A $1M deal with Hooli Corp for 5,000 user seats.

Key Requirements: Bulk GitHub seat reclamation, SOC2 compliance, and 99.9% verified uptime.

The 'Truth' in Logs: * Slack: Nitin instructs the team to focus 100% on Hooli and apply a 15% discount for a 3-year commitment.

GitHub: Logic implemented in GitHubManager for bulk archival and SecurityManager for AES-256 GCM encryption.

AI Goal: Detect if the departing employee understands the specific pricing tiers and the "soft-delete" safety gates promised to Hooli.

2. Project Phoenix & The Legacy Patch (The Technical Baseline)
The Context: A confidential security project.

The 'Secret' (Private Slack): Project Phoenix was delayed to Q4 because the team had to divert senior devs to silently patch a vulnerability in the legacy HRIS login system.

The 'Official' Version: Publicly, the delay is attributed to "feature refinement."

The 'Truth' in Logs:

Slack (Private): Nitin and Mithilesh discuss the "silent patch" and the merger with Apex Cloud.

GitHub: LegacyHRISHandler contains a "secure login bridge" that diverts traffic to a v2 validator.

AI Goal: Identify if the employee is transparent about the true reason for the project delay or if they are hiding "Shadow Risks."
