from scraper import Scraper


# Entry point
if __name__ == '__main__':

    # Run the main logic
    try:
        bot = Scraper()
        bot.run()

    except KeyboardInterrupt:
        print("Close")
