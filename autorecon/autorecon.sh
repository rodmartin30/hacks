#!/bin/bash

# Create directory for the target.
root_dir=~/recon/$1
mkdir -p $root_dir
cd $root_dir

# -------- Subdomain discovery --------
# Amass
echo "Starting amass..."
amass_dir=$root_dir/amass
mkdir -p $amass_dir
cd $amass_dir
amass enum -o out -d $1
cat < out >> ../domains

# Assetfinder
echo "Starting assetfinder..."
asset_finder_dir=$root_dir/asset_finder
mkdir -p $asset_finder_dir
cd $asset_finder_dir
assetfinder --subs-only $1
cat < out >> ../domains

# findomain
echo "Starting findomain..."
findomain_dir=$root_dir/findomain
mkdir -p $findomain_dir
cd $finddomain_dir
findomain -t $1 -o
cat < $1.txt >> ../domains

# subbrute
echo "Starting subbrute..."
subbrute_dir=$root_dir/subbrute
mkdir -p $subbrute_dir
cd $subbrute_dir
subbrute.py $1 -o out -r ~/tools/subbrute/resolvers.txt
cat < out >> ../domains

# crt.sh
echo "Starting crt..."
crt_dir=$root_dir/crt_dir
mkdir -p $crt_dir
cd $crt_dir
curl -s https://crt.sh/\?q\=\%.$1\&output\=json | gron | grep "\.name_value =" | cut -d "\"" -f 2 | sed "s/^\*\.//" | sort -u | tee out | anew ../domains

# waybackurl
echo "Running waybackurl..."
waybackurl_dir=$root_dir/waybackurl
cd $root_dir
waybackurl $1 | cut -d "/" -f 3 | tee $waybackurl_dir/out | anew ../domains

# -------- Hosts discovery --------
echo "Running hosts discovery..."
cd $root_dir
sort -u domains -o domains
cat domains | httprobe | tee hosts

# -------- Port discovery --------
echo "Running ports discovery on hosts..."
# Run nmap with low velocity just to gather which ports are open, then add -A
# sudo nmap -sV -T2 -p- 
