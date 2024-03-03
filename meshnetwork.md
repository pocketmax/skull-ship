

* network is pull based meaning blocks move from one node to another based on request for it
* no device authentication. anyone can connect to anyone
* (possibly) devices are identified with PKI
* users are identified with PKI but mesh has no awareness of them
* popularity drives network. popular blocks are in areas where they are needed. less popular blocks are in less needed

# OSI layers

layer 7: application (http, https, bluetooth)
layer 6: presentation (skip it since assets can be encrypted)
layer 5: session (skip it since all transmissions are stateless)
layer 4: transport (skip it since error checking is handled on devices)
layer 3: network (block IDs and asset IDs)
layer 2: data link (device IDs i.e. MAC address, bluetooth ID, lora ID)
layer 1: physical (radio, cable)

## what is the incentive to participate?
* the more you route traffic, the priority for your personal traffic increases i.e. published blocks, fetched blocks

## data fields used to help route blocks through the network
* signal strength from neighbors
* successful block pull matches (when a pulled block reaches it's requester)
* block size
* device capacity
* throughput

## app examples
* youtube
* facebook

## types of apps (block schema aware)
* web browser
* mobile app
* desktop app
* car apps

## types of connection media (device aware)
* wifi
* wireless
* cellular 4G+
* lora wireless
* bluetooth
* TV antenna
* long piece of string

## types of devices (connection aware)
* tablets
* phones
* playstation
* cars
* laptops
* PCs
* raspberry pi
* arduino
* two tin cans

## types of network payloads (read/requested/created by apps)
* block (holds collection of hashes)
* asset (generic blob)

## types of asset media on mesh
* plain text i.e. HTML, chat message (can contain hashes to later be resolved)
* blob
* software updates

## network commands
* current manifest (list of IDs I have)
* needed manifest (list of IDs I need)
* get asset
* put asset
* get block
* put block