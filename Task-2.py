import numpy as np

u = np.array([8,2,5],dtype=float)
print(u.shape)

AAction = np.array([9,1,2],dtype=float)
print(AAction.shape)

BComedy = np.array([1,9,8],dtype=float)
print(BComedy.shape)

CDrama = np.array([7,2,6],dtype=float)
print(CDrama.shape)

def cos (user: np.ndarray, film: np.ndarray ) -> float:
    dot = np.dot(user, film)
    norm = np.linalg.norm(user) * np.linalg.norm(film)

    return dot/norm

cosAAction = cos(u, AAction)
print(f"Фільм A Action: {cosAAction:.4f}")

cosBComedy = cos(u,BComedy)
print(f"Фільм B Comedy: {cosBComedy:.4f}")

cosCDrama = cos(u,CDrama)
print(f"Фільм C Drama: {cosCDrama:.4f}")

scores = {
    "Фільм A Action": cosAAction,
    "Фільм B Comedy": cosBComedy,
    "Фільм C Drama": cosCDrama,
}

best = max(scores, key=lambda name: scores[name])
best_score = scores[best]
print(f"\nНайбільш схожий фільм: {best} ({best_score:.4f})")