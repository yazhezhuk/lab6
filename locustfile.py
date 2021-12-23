
import time

from locust import HttpUser, task

base_url = "https://gorest.co.in/public/v1"
bearer_token = "c61fee699bc87434570db5d3f83fc05ba7be3a4111571baf6b5cea49fe03137f"


class SomeUser(HttpUser):

    @task
    def get(self):
        self.client.get("/users",headers={"Authorization": "Bearer " + bearer_token})

    @task
    def view_users(self):
        for user_id in range(100):
            self.client.get(f"/users/{user_id}",headers={"Authorization": "Bearer " + bearer_token})
            time.sleep(1)

    @task
    def add_posts(self):
        for post_id in range(100):
            self.client.post(f"/posts/", name="/posts", json={"id": post_id, "email": post_id,"body" : post_id}, headers={"Authorization": "Bearer " + bearer_token})
            time.sleep(1)

    @task
    def put_users(self):
        for user_id in range(100):
            self.client.put(f"/users/{user_id}",
                            json={"username": f"f{user_id}", "password": f"b {user_id}"}, headers={"Authorization": "Bearer " + bearer_token})
            time.sleep(1)

    @task
    def put_comments(self):
        for post_id in range(100):
            self.client.delete(f"/posts/{post_id}", name="/posts",headers={"Authorization": "Bearer " + bearer_token})
            time.sleep(1)

    def on_start(self):
        self.client.headers = {'Authorization': "Bearer " + bearer_token}
# users test
