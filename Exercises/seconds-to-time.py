def main():
    seconds = float(input("Seconds: "))
    hours = seconds / 3600
    minutes = (hours - int(hours)) * 30 / 0.5
    seconds = (minutes - int(minutes)) * 30 / 0.5

    hours = str(int(round(hours, 6)))
    minutes = str(int(round(minutes, 6)))
    seconds = str(int(round(seconds, 6)))

    result = ":".join(n if len(n) > 1 else f"0{n}" for n in (hours, minutes, seconds))
    print(result)


if __name__ == '__main__':
    main()
