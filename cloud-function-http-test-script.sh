curl -X POST https://us-central1-athegiamedical.cloudfunctions.net/save_biometrics_to_firestore \
 -H 'Content-Type: application/json' -d '{"data":{"patient_uuid":"aaabbbccdddeeefff", "timestamp":"2019-12-14 13:48:00.267830","payload":{"result":{"key1":"this is key 1", "key2":"this is key2"}}}}'  