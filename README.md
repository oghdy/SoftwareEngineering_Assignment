# 소프트웨어공학 개인 실습 과제 1: 일상 속 소프트웨어 사용 사례 - 카페 키오스크 음료 주문 시스템

## 1. 주제 선정 및 설계 의도
본 과제에서는 일상에서 흔히 접하는 소프트웨어 중 하나인 카페 키오스크의 음료 주문 과정을 선정하여 시스템을 모델링하고 구현했습니다. 
사용자가 메뉴를 선택하고, 결제하며, 음료가 제조되는 일련의 과정을 소프트웨어적으로 표현하고자 했습니다.
특히, 시스템 설계 시 모듈 간의 낮은 결합도와 높은 응집도를 지향하며, 추후 시스템 확장 및 유지보수를 용이하게 하는 데 중점을 두었습니다.

## 2. 시퀀스 다이어그램 모델링

Mermaid.live를 활용하여 모델링한 시퀀스 다이어그램입니다. 
사용자(User)와 주요 시스템 구성 요소들(KioskUI, MenuManager, OrderProcessor, PaymentGateway, BeverageMaker) 간의 메시지 흐름을 시각화했습니다.
```mermaid
sequenceDiagram
    actor User
    participant KioskUI
    participant MenuManager
    participant OrderProcessor
    participant PaymentGateway
    participant BeverageMaker

    User->>KioskUI: 메뉴 선택 (예: 아메리카노)
    KioskUI->>MenuManager: 선택된 메뉴 정보 요청
    MenuManager-->>KioskUI: 메뉴 정보 반환 (가격, 재고 등)
    KioskUI->>OrderProcessor: 주문 생성 요청 (메뉴, 수량)
    OrderProcessor-->>KioskUI: 주문 정보 반환 (주문 ID, 총액)
    User->>KioskUI: 결제 방식 선택 (예: 카드)
    KioskUI->>OrderProcessor: 결제 요청 (주문 ID, 결제 방식)
    OrderProcessor->>PaymentGateway: 결제 승인 요청
    PaymentGateway-->>OrderProcessor: 결제 승인 응답
    OrderProcessor-->>KioskUI: 결제 완료 알림
    OrderProcessor->>BeverageMaker: 음료 제조 요청 (메뉴, 수량)
    BeverageMaker-->>OrderProcessor: 음료 제조 완료 알림
    KioskUI-->>User: 주문 완료 메시지 표시

## 3. 샘플 코드 구현

위 시퀀스 다이어그램을 기반으로 Python으로 구현된 샘플 코드입니다. 각 참여자(액터, 객체)는 클래스로, 메시지 교환은 메서드 호출로 매핑했습니다.

<파일 구조>
.
├── menu_manager.py
├── order_processor.py
├── payment_gateway.py
├── beverage_maker.py
└── kiosk_ui.py (메인 실행 파일)

<주요 모듈 설명>
kiosk_ui.py: 사용자와의 상호작용 및 전체 주문 흐름을 제어하는 사용자 인터페이스 역할을 수행합니다.
실제 카페 키오스크에서 사용자가 가장 자주 겪는 흐름(메뉴 선택 → 수량 → 결제 방식 선택)에 맞춰 사용자 흐름을 자연스럽게 구성하고자 했습니다.

menu_manager.py: 카페 메뉴 정보(이름, 가격, 재고)를 관리하고 제공합니다.

order_processor.py: 주문 생성, 결제 처리 요청, 음료 제조 요청 등 주문의 핵심 비즈니스 로직을 처리합니다.
OrderProcessor는 주문, 결제, 제조와 관련된 다양한 객체들 (PaymentGateway, BeverageMaker) 간의 복잡한 상호작용을 중재하고 조정하는 조정자(Mediator) 패턴의 역할에 가깝게 설계되었습니다.
이를 통해 각 객체 간의 직접적인 결합을 줄이고 시스템의 유연성을 높였습니다.

payment_gateway.py: 가상의 외부 결제 시스템과의 연동을 담당합니다.
향후 다양한 결제 수단(예: 신용카드, 모바일 페이, 간편 결제)을 유연하게 추가하고 관리할 수 있도록 전략(Strategy) 패턴을 적용하여 확장 가능하도록 고려되었습니다.
현재는 단일 PaymentGateway 구현체만을 포함하고 있지만, IPaymentGateway와 같은 인터페이스를 정의하고 이를 구현하는 방식으로 확장이 용이합니다.

beverage_maker.py: 가상의 음료 제조 시스템을 시뮬레이션합니다.

<코드 실행 방법>
-모든 .py 파일을 GitHub 저장소에서 클론하거나 다운로드합니다.
-터미널 또는 명령 프롬프트에서 kiosk_ui.py 파일이 있는 디렉토리로 이동합니다.
-다음 명령어를 입력하여 프로그램을 실행합니다.
 python kiosk_ui.py
-화면의 지시에 따라 메뉴를 선택하고 주문을 진행합니다.

## 4. 샘플 코드 모듈 평가
구현된 샘플 코드의 응집도와 결합도를 소프트웨어공학적 관점에서 평가했습니다.
응집도 (Cohesion)
대부분의 클래스는 단일 책임을 가지고 있거나, 관련된 책임들을 응집력 있게 묶어두고 있습니다.
-높은 응집도: MenuManager, PaymentGateway, BeverageMaker 클래스는 각각 메뉴 관리, 결제 요청, 음료 제조라는 명확하고 단일한 책임을 가지므로 높은 응집도를 보입니다.
-비교적 높은 응집도: OrderProcessor는 주문 생성, 결제 처리 조정, 음료 제조 요청 등 '주문 처리'와 관련된 여러 책임을 수행하지만,
 이 책임들이 논리적으로 밀접하게 연관되어 있어 비교적 높은 응집도를 유지합니다. KioskUI는 사용자 인터페이스 상호작용 및 전체 시스템 흐름 제어라는 책임을 가지며, 이 또한 응집력이 높은 편입니다.

결합도 (Coupling)
모듈 간의 의존성을 최소화하여 낮은 결합도를 유지하려고 노력했습니다.
-낮은 결합도: OrderProcessor는 PaymentGateway와 BeverageMaker 객체를 생성자 주입(Dependency Injection) 방식으로 받아서 사용합니다.
 이는 직접적인 클래스 생성 대신 외부에서 의존성을 주입받는 형태로, 낮은 결합도를 유지하는 데 기여합니다.
-각 모듈은 다른 모듈의 내부 구현에 대해 알 필요 없이, 공개된 인터페이스(메서드)를 통해서만 상호작용합니다.
 예를 들어, OrderProcessor는 PaymentGateway.request_payment()를 호출할 뿐,PaymentGateway가 어떻게 결제를 처리하는지에 대한 세부 사항은 알지 못합니다.
-전반적으로 각 클래스가 독립적으로 기능하며, 필요한 경우에만 다른 클래스와 최소한의 인터페이스를 통해 통신하므로 낮은 결합도를 유지합니다.

추가적인 개선 고려사항 (테스트 및 에러 처리)
현재 샘플 코드에는 간단한 사용자 입력 유효성 검사와 기본적인 예외 처리 (try-except)가 포함되어 있습니다.
실제 상용 시스템에서는 InvalidInputError, OrderProcessingError와 같은 사용자 정의 예외 클래스를 도입하여 더욱 구조화된 예외 처리를 구현하고, logging 모듈을 활용한 상세한 로그 시스템을 구축하여 시스템의 안정성과 문제 진단 기능을 강화할 수 있습니다.
또한, 각 모듈의 기능이 올바르게 동작하는지 확인할 수 있는 단위 테스트(Unit Test) 코드를 작성하는 것도 중요합니다.

5. 결론
본 과제를 통해 일상 속 소프트웨어 사용 사례를 분석하고, 이를 시퀀스 다이어그램으로 모델링하며, 실제 코드로 구현하는 과정을 경험할 수 있었습니다.
특히, 응집도와 결합도와 같은 소프트웨어 설계 원칙뿐만 아니라, 디자인 패턴(조정자, 전략)과 사용자 중심 경험(UX), 그리고 견고한 예외 처리 및 로깅의 중요성을 이해하는 계기가 되었습니다.
이는 단순히 기능을 구현하는 것을 넘어, 확장 가능하고 유지보수하기 쉬운 소프트웨어를 개발하는 데 필수적인 요소임을 다시 한번 깨달았습니다.





