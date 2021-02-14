T = int(input())

seat_types = {
  'WS': [1, 6, 7, 0],
  'MS': [2, 5, 8, 11],
  'AS': [3, 4, 9, 10]
}
seats = []

for t in range(T):
  seats.append(int(input()))

for seat in seats:
  for seat_type in seat_types:
    try:
      mod = seat % 12
      seat_types[seat_type].index(mod)
      facing_seat = seat - mod

      if mod:
        facing_seat += 13 - mod
      else:
        facing_seat -= 11

      print(facing_seat, seat_type)
    except ValueError:
      pass
