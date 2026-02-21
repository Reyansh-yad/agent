happy(yogita).
listen2Music(ria).
listen2Music(yogita):- happy(yogita).
playsAirGuitar(ria):- listen2Music(ria).
playsAirGuitar(yogita):-listen2Music(yogita).
