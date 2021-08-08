# Simple KV Service
Simple KV service written with Flask and Sqlite. Service can be accessed via HTTP and CLI Packaged in same repo.

Topic:  
[Index](readme.md) | [CLI](cli.md)| [Deployment](deployment.md)

---

## Deployment

This service does'nt support replication and multiple node setup, hence its state is emphemeral and we will loose data on instance deletion. Kubernetes may help with `statefulset` to mount the `sqlite` File on cluster with protection from accidental delete. But for AWS EC2, We may required to put some ASG lifecyle to backup the `sqlite` file on Deletion and restore on instance bootstrap.



### AWS 