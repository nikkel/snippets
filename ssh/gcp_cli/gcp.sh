# VM Commands

# List all the current regions and zones
gcloud compute zones list

# List all the current regions and zone with a filter 
gcloud compute zones list | grep us-central1

# Set your default deployment location of VM
gcloud config set compute/zone us-central1-b

# Create a new VM
gcloud compute instances create "my-vm-2" \
--machine-type "n1-standard-1" \
--image-project "debian-cloud" \
--image-family "debian-10" \
--subnet "default"