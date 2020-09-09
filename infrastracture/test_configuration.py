from infrastracture.configuration import config

desired_capabilities = {"platformVersion": config.get("infra").get("version"),
                        "deviceName": "emulator-5554",
                        "app": config.get("infra").get("file_path"),
                        "platformName": config.get("infra").get("platform"),
                        "autoGrantPermissions": "true"
                        }

email = config.get("user").get("email")
password = config.get("user").get("password")