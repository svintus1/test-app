**Version 1.0**  
**Last Updated**: 28.03.2025
- [English](#English)
- [Russian](#Russian)
# English
---
## **1. Project Overview**  
### **Core Concept**  
"Bunker Online" is a survival-themed multiplayer card game where players compete to secure a spot in a bunker during an impending catastrophe. The primary goal is to **demonstrate full-stack development skills** (FastAPI/React) and **DevOps/CI-CD practices** while creating a functional, engaging pet project.  

#### **Objectives**  
1. Develop a working web app to showcase technical proficiency.  
2. Implement DevOps pipelines (CI/CD) for automated testing and deployment.  
3. Create a simple but entertaining game for friends to playtest.  

---

## **2. Target Audience**  
- **Primary Audience**: Friends and peers (initial testing group).  
- **Secondary Audience**: Developers/recruiters reviewing the project as a portfolio piece.  

---

## **3. Game Rules & Mechanics**  
### **Game Flow**  
1. **Lobby Setup**:  
   - Players (4–16) join a game room.  
   - Assign unique characters with traits:  
     - Profession (e.g., Doctor, Engineer).  
     - Health status (e.g., "Asthmatic," "Immune to Radiation").  
     - Hobbies (e.g., Gardening, Lockpicking).  
     - Personal item (e.g., Flashlight, First Aid Kit).  

2. **Catastrophe Announcement**:  
   - Reveal the disaster type (e.g., Nuclear Fallout, Zombie Outbreak).  

3. **Discussion Phase**:  
   - Players debate their value to the bunker using character traits.  
   - Optional time limit (e.g., 2 minutes per round).  

4. **Voting Phase**:  
   - Players vote to eliminate one participant.  
   - Tiebreaker: Random selection or revote.  

5. **Elimination**:  
   - Eliminated players remain in the room as observers (greyed-out avatars).  

6. **Winning Condition**:  
   - Game ends when surviving players match bunker capacity (e.g., 4 survivors for a 6-player game).  

---

## **4. Features & Functionality**  
### **Player-Facing Features**  
| Feature                | Description                                                                 | Priority |  
|-------------------------|-----------------------------------------------------------------------------|----------|  
| **Lobby System**        | Create/join rooms with unique IDs.                                          | P0       |  
| **Character Cards**     | Display traits (profession, health, etc.) in a hand UI.                     | P0       |  
| **Dynamic Avatars**     | Show player avatars; grey out eliminated players.                           | P0       |  
| **Card Reveal**         | Players can "show" cards to all participants during discussions.            | P1       |  
| **Animations**          | Smooth card flips, vote transitions, and elimination effects.               | P2       |  
| **Basic Chat**          | Optional text chat (voice chat handled externally via Discord/Zoom).         | P3       |  

### **Technical Features**  
| Feature                | Description                                                                 |  
|-------------------------|-----------------------------------------------------------------------------|  
| **Scalable Backend**    | FastAPI + WebSocket architecture for real-time sync (designed for future scaling). |  
| **Character Generator** | Algorithm to randomize traits and ensure uniqueness.                        |  
| **Voting System**       | Secure vote tallying and real-time results broadcast.                       |  

---

## **5. Technical Architecture**  
### **Frontend**  
- **Framework**: React (TypeScript) for CSR.  
- **Styling**: TailwindCSS for rapid UI development.  
- **Real-Time**: WebSocket integration for game state updates.  

### **Backend**  
- **Framework**: FastAPI (Python).  
- **Database**: PostgreSQL + SQLModel (ORM).  
- **APIs**:  
  - **HTTP**: Room creation, character assignment.  
  - **WebSocket**: Real-time voting, discussion, and state sync.  

### **DevOps**  
- **CI/CD**: GitHub Actions/GitLab CI for automated testing and deployment.  
- **Infrastructure**:  
  - Docker containers for backend/frontend.  
  - Reverse proxy (Nginx) + ASGI server (Uvicorn).  
  - Hosting: VPS or Self-hosted

---

## **6. User Experience (UX)**  
### **User Stories**  
1. *"As a player, I want to join a game room via a link so I can play with friends."*  
2. *"As a player, I want to see my character’s traits and argue my case during discussions."*  
3. *"As a developer, I want to ensure the game state syncs in real-time to avoid desync issues."*  

### **UI Mockups (Key Screens)**  
1. **Lobby Screen**: Room code, player avatars, "Start Game" button.  
2. **Game Screen**:  
   - Player’s hand (character cards).  
   - Central area for revealed cards/animations.  
   - Voting UI (buttons or card selection).  
3. **Elimination Screen**: Greyed-out avatars with "Spectator" label.  

---

## **7. Roadmap**  
| Phase      | Milestone                                   | Timeline |  
|------------|---------------------------------------------|----------|  
| **Alpha**  | Core gameplay loop (no animations).         | 2 weeks  |  
| **Beta**   | Polish UI, add voting/elimination logic.    | 3 weeks  |  
| **v1.0**   | Animations, DevOps pipeline, friend testing.| 4 weeks  |  

---

## **8. Risks & Mitigations**  
| Risk                          | Mitigation                                                                 |  
|-------------------------------|---------------------------------------------------------------------------|  
| WebSocket disconnects          | Implement reconnection logic and session recovery.                       |  
| Character trait collisions     | Use a uniqueness check in the generator algorithm.                       |  
| Scalability bottlenecks        | Design stateless backend services; containerize early.                   |  

---

## **9. Compliance**  
- **Data Privacy**: No analytics or user data storage. GDPR compliance not required (friends-only).  
- **Licensing**: Open-source code (MIT License) for portfolio visibility.  

---

## **10. Success Metrics**  
1. Functional MVP playable by friends.  
2. Full CI/CD pipeline implementation.  
3. Positive feedback on code quality and gameplay from peer reviewers.  

--- 

### **Next Steps**  
1. Finalize character trait list.  
2. Draft API endpoints (HTTP + WebSocket).  
3. Set up GitHub repo with Docker/CI-CD scaffolding.  

# Russian
---
## **1. Обзор проекта**  
### **Основная концепция**  
"Bunker Online" — это многопользовательская карточная игра в жанре выживания, где игроки соревнуются за место в бункере во время надвигающейся катастрофы. Основная цель — **продемонстрировать навыки full-stack разработки** (FastAPI/React) и **практики DevOps/CI-CD**, создавая при этом функциональный и увлекательный пет-проект.  

#### **Цели**  
1. Разработать рабочее веб-приложение для демонстрации технических навыков.  
2. Реализовать DevOps-процессы (CI/CD) для автоматизированного тестирования и развертывания.  
3. Создать простую, но интересную игру для тестирования с друзьями.  

---

## **2. Целевая аудитория**  
- **Основная аудитория**: Друзья и коллеги (первоначальная тестовая группа).  
- **Вторичная аудитория**: Разработчики/рекрутеры, оценивающие проект как часть портфолио.  

---

## **3. Правила и механика игры**  
### **Игровой процесс**  
1. **Создание лобби**:  
   - Игроки (4–16) присоединяются к игровой комнате.  
   - Каждому назначается уникальный персонаж с характеристиками:  
     - Профессия (например, Врач, Инженер).  
     - Состояние здоровья (например, "Астматик", "Устойчив к радиации").  
     - Хобби (например, Садоводство, Взлом замков).  
     - Личный предмет (например, Фонарик, Аптечка).  

2. **Объявление катастрофы**:  
   - Раскрывается тип катастрофы (например, Ядерная зима, Зомби-апокалипсис).  

3. **Фаза обсуждения**:  
   - Игроки аргументируют свою ценность для бункера, используя характеристики персонажа.  
   - Опциональное ограничение времени (например, 2 минуты на раунд).  

4. **Фаза голосования**:  
   - Игроки голосуют за исключение одного участника.  
   - При ничьей: случайный выбор или переголосование.  

5. **Исключение**:  
   - Исключенные игроки остаются в комнате как наблюдатели (аватары серого цвета).  

6. **Условие победы**:  
   - Игра завершается, когда число выживших соответствует вместимости бункера (например, 4 выживших в игре на 6 игроков).  

---

## **4. Функционал и возможности**  
### **Функции для игроков**  
| Функция                | Описание                                                                 | Приоритет |  
|-------------------------|---------------------------------------------------------------------------|----------|  
| **Система лобби**       | Создание/вход в комнаты с уникальными ID.                                | P0       |  
| **Карты персонажей**    | Отображение характеристик (профессия, здоровье и т.д.) в интерфейсе.     | P0       |  
| **Динамические аватары**| Отображение аватаров игроков; исключенные игроки серого цвета.           | P0       |  
| **Раскрытие карт**      | Игроки могут "показывать" карты всем участникам во время обсуждения.     | P1       |  
| **Анимации**            | Плавные перевороты карт, переходы при голосовании, эффекты исключения.   | P2       |  
| **Чат**                 | Опциональный текстовый чат (голосовой чат через Discord/Zoom).           | P3       |  

### **Технические функции**  
| Функция                | Описание                                                                 |  
|-------------------------|---------------------------------------------------------------------------|  
| **Масштабируемый бэкенд** | FastAPI + WebSocket для синхронизации в реальном времени (с заделом на масштабирование). |  
| **Генератор персонажей** | Алгоритм для рандомизации характеристик и обеспечения уникальности.      |  
| **Система голосования**  | Безопасный подсчет голосов и трансляция результатов в реальном времени. |  

---

## **5. Техническая архитектура**  
### **Фронтенд**  
- **Фреймворк**: React (TypeScript) для CSR.  
- **Стилизация**: TailwindCSS для быстрой разработки UI.  
- **Реальное время**: Интеграция WebSocket для обновления состояния игры.  

### **Бэкенд**  
- **Фреймворк**: FastAPI (Python).  
- **База данных**: PostgreSQL + SQLModel (ORM).  
- **API**:  
  - **HTTP**: Создание комнат, назначение персонажей.  
  - **WebSocket**: Голосование, обсуждение и синхронизация состояния.  

### **DevOps**  
- **CI/CD**: GitHub Actions/GitLab CI для автоматизированного тестирования и развертывания.  
- **Инфраструктура**:  
  - Docker-контейнеры для бэкенда/фронтенда.  
  - Обратный прокси (Nginx) + ASGI-сервер (Uvicorn).  
  - Хостинг: VPS или хостим сами
---

## **6. Пользовательский опыт (UX)**  
### **Сценарии использования**  
1. *"Как игрок, я хочу присоединиться к игровой комнате по ссылке, чтобы играть с друзьями."*  
2. *"Как игрок, я хочу видеть характеристики своего персонажа и аргументировать свою позицию во время обсуждения."*  
3. *"Как разработчик, я хочу обеспечить синхронизацию состояния игры в реальном времени, чтобы избежать рассинхронизации."*  

### **Макеты интерфейса (ключевые экраны)**  
1. **Экран лобби**: Код комнаты, аватары игроков, кнопка "Начать игру".  
2. **Игровой экран**:  
   - Рука игрока (карты персонажа).  
   - Центральная область для раскрытых карт/анимаций.  
   - Интерфейс голосования (кнопки или выбор карт).  
3. **Экран исключения**: Серые аватары с пометкой "Наблюдатель".  

---

## **7. План разработки**  
| Этап       | Веха                                      | Сроки     |  
|------------|-------------------------------------------|----------|  
| **Альфа**  | Базовая игровая механика (без анимаций).  | 2 недели |  
| **Бета**   | Доработка UI, логика голосования/исключения. | 3 недели |  
| **v1.0**   | Анимации, DevOps-процессы, тестирование с друзьями. | 4 недели |  

---

## **8. Риски и решения**  
| Риск                          | Решение                                                                 |  
|-------------------------------|-------------------------------------------------------------------------|  
| Разрывы соединения WebSocket   | Реализация логики переподключения и восстановления сессии.             |  
| Коллизии характеристик        | Проверка уникальности в алгоритме генерации.                           |  
| Проблемы масштабируемости     | Статус-независимый бэкенд; ранняя контейнеризация.                     |  

---

## **9. Соответствие требованиям**  
- **Конфиденциальность данных**: Нет аналитики или хранения пользовательских данных. GDPR не требуется (только для друзей).  
- **Лицензирование**: Открытый исходный код (лицензия MIT) для видимости в портфолио.  

---

## **10. Критерии успеха**  
1. Рабочий MVP, пригодный для игры с друзьями.  
2. Полноценный CI/CD-процесс.  
3. Положительные отзывы о качестве кода и игрового процесса от тестировщиков.  

--- 

### **Следующие шаги**  
1. Финализировать список характеристик персонажей.  
2. Определить API-эндпоинты (HTTP + WebSocket).  
3. Настроить репозиторий GitHub с инфраструктурой Docker/CI-CD.  