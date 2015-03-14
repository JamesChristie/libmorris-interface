from arenalib.entities.label import Label

def build_titles():
  return [upper_title(), middle_title(), lower_title()]

def upper_title():
  return Label(
    0.5, 0.75,
    "Staying up WAY too late presents:"
  )

def middle_title():
  return Label(
    0.5, 0.5,
    "T3Arena",
    large=True
  )

def lower_title():
  return Label(
    0.5, 0.25,
    "(Click to Continue)"
  )
