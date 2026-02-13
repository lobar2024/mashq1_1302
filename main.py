repo = InMemoryTaskRepo()
svc = TaskService(repo)

t = svc.create("hello")
assert t is not None
assert t.id == 1

ok = svc.mark_done(1)
assert ok is True

ok = svc.mark_done(999)
assert ok is False

done, total = svc.summary()
assert done == 1
assert total == 1

print("testlar ok")
