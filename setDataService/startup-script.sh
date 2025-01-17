# Copyright 2019 Google LLC All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Echo commands and fail on error
set -ev

# [START getting_started_gce_startup_script]
# Install or update needed software
apt-get update
apt-get install -yq git supervisor python python-pip python3-distutils
pip install --upgrade pip virtualenv

# Fetch source code
mkdir /opt/app
gsutil -m cp -r gs://buck-soa-final-368610/SOA_Proyecto3/* /opt/app
# Install Cloud Ops Agent
sudo bash /opt/app/setDataService/add-google-cloud-ops-agent-repo.sh --also-install

# Account to own server process
useradd -m -d /home/pythonapp pythonapp

# Python environment setup
virtualenv -p python3 /opt/app/setDataService/env
/bin/bash -c "source /opt/app/setDataService/env/bin/activate"
/opt/app/setDataService/bin/pip install -r /opt/app/setDataService/requirements.txt

# Set ownership to newly created account
chown -R pythonapp:pythonapp /opt/app

# Put supervisor configuration in proper place
cp /opt/app/setDataService/python-app.conf /etc/supervisor/conf.d/python-app.conf

# Start service via supervisorctl
supervisorctl reread
supervisorctl update
# [END getting_started_gce_startup_script]
supervisorctl reread
supervisorctl update
# [END getting_started_gce_startup_script]