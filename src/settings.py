from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    BOT_TOKEN: str
    API_KEY_CHATGPT: str
    API_KEY_GEMINI: str
    API_KEY_KADINSKY: str
    API_SECRET_KEY_KADINSKY: str

    DB_HOST: str
    DB_PORT: str
    DB_USER: str
    DB_PASS: str
    DB_NAME: str

    @property
    def DB_URL(self):
        return f"postgresql://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
