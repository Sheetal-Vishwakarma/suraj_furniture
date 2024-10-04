#!/bin/bash

if [ -d "/home/admin/hrms-revamp-2024" ]; then
    rm -rf "/home/admin/hrms-revamp-2024"
    echo "Directory deleted successfully."
fi

git clone https://hrmsrevamp2024-prod-pat-auth:glpat-ZNsyiCSVHgMS3Yx_bA8c@code.netscribes.info/engineering/internal/hrms-revamp-2024.git

echo "echo $?"

ls -ld /home/admin/hrms-revamp-2024

echo "git clone completed"

chown -R admin:admin /home/admin/hrms-revamp-2024 && chmod -R 775  /home/admin/hrms-revamp-2024

echo "echo $?"

