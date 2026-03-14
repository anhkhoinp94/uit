# I. Fundamentals – Design Principles & Patterns
SOLID là gì và tại sao nó quan trọng trong thiết kế phần mềm?
Single Responsibility Principle(SRP) là gì? Cho ví dụ trong service design.
Open/Closed Principle(OCP) là gì? Làm sao để mở rộng code mà không sửa code cũ?
Liskov Substitution Principle(LSP) nghĩa là gì? Khi nào subclass có thể gây bug?
Interface Segregation Principle(ISP) giải quyết vấn đề gì trong thiết kế API?
Dependency Inversion Principle(DIP) khác gì dependency injection?
Làm sao áp dụng SOLID khi thiết kế microservice?
SRP ảnh hưởng thế nào đến việc chia service trong microservices?
DIP giúp test hệ thống dễ hơn như thế nào?
ISP giúp thiết kế API client tốt hơn ra sao?
Khi nào việc áp dụng SOLID quá mức gây over-engineering?
Trong hệ thống lớn, làm sao giữ codebase vẫn tuân theo SOLID?
SOLID có áp dụng được cho distributed system không? Nếu có thì như thế nào?
Khi thiết kế domain service lớn, làm sao tránh vi phạm SRP?
Trong microservices architecture, DIP có thể áp dụng ở level service communication như thế nào?
Design pattern là gì và tại sao nó quan trọng trong system design?
Singleton pattern dùng khi nào? Khi nào không nên dùng?
Factory pattern giúp giải quyết vấn đề gì?
Builder pattern khác gì constructor truyền nhiều tham số?
Strategy pattern dùng khi nào trong business logic?
Dependency Injection pattern giúp code dễ test như thế nào?
Adapter pattern dùng khi tích hợp hệ thống legacy như thế nào?
Facade pattern giúp đơn giản hóa hệ thống lớn ra sao?
Repository pattern có vai trò gì trong clean architecture?


# II. Programming Languages & Frameworks (Python/FastAPI + Golang)
FastAPI hoạt động dựa trên ASGI như thế nào?
async / await trong Python hoạt động ra sao?
Khi nào nên dùng async ? Khi nào không?
So sánh FastAPI và Flask về performance và concurrency.
Dependency Injection trong FastAPI là gì?
Pydantic validation hoạt động như thế nào?
Middleware trong FastAPI dùng để làm gì?
Làm sao tối ưu performance API Python?
GIL là gì? Nó ảnh hưởng thế nào tới multi-threading?
multiprocessing vs threading trong Python.
Cách implement background tasks trong FastAPI.
Rate limiting trong API nên làm ở đâu?
Làm sao handle global exception trong FastAPI?
Làm sao viết API versioning?
Bạn sẽ test API như thế nào(unit/integration)?
Python memory management hoạt động thế nào?
Reference counting và garbage collector khác nhau ra sao?
Mutable vs immutable ảnh hưởng thế nào đến performance và bug?
Deep copy vs shallow copy khác nhau thế nào?
Khi nào gây bug khó phát hiện?
Decorator hoạt động ra sao?
Ứng dụng thực tế trong logging, auth, caching?
Context manager là gì?
Khi nào nên tự viết context manager?
Metaclass là gì?
Khi nào thực sự cần dùng Metaclass?
Monkey patching là gì?
Khi nào nên và không nên dùng Monkey patching?
Python import system hoạt động thế nào?
Circular import xử lý ra sao?
Typing(type hints) giúp gì trong dự án lớn?
Khi nào nên dùng mypy?
Dataclass vs Pydantic vs NamedTuple khác nhau thế nào?
Concurrency trong Python gồm những mô hình nào?
Async IO vs threading vs multiprocessing khác nhau ra sao trong thực tế?
Event loop hoạt động như thế nào?
Blocking call ảnh hưởng gì đến async app?
Làm sao detect memory leak trong Python?
Profiling Python code bằng cProfile hoặc line_profiler như thế nào?
Time complexity ảnh hưởng thế nào đến API performance?
Thiết kế project structure cho ứng dụng lớn như thế nào?
Làm sao tách business logic khỏi framework(clean architecture)?
Dependency injection trong Python thuần(không dùng FastAPI) làm thế nào?
Khi nào nên dùng class, khi nào nên dùng function thuần?
Làm sao viết code Python thread-safe?
Gunicorn vs Uvicorn khác nhau thế nào?
Worker type ảnh hưởng ra sao?
WSGI vs ASGI khác nhau thế nào?
Làm sao scale Python app khi GIL tồn tại?
Khi nào cần dùng C extension hoặc Cython?
Mock vs patch khác nhau thế nào?
Test async function như thế nào?
Property-based testing là gì?
Coverage cao có đảm bảo code tốt không?
Closure là gì và được dùng để làm gì?
NumPy là gì? Tại sao nên dùng NumPy thay vì Python list?
ndarray trong NumPy là gì? Nó khác gì với list trong Python?
Vectorization trong NumPy là gì? Vì sao nó nhanh hơn loop Python?
Broadcasting trong NumPy là gì?
Shape và dtype của một array là gì?
Sự khác nhau giữa reshape() và resize() trong NumPy?
Slicing trong NumPy khác gì với slicing của Python list?
Copy vs View trong NumPy là gì?
Khi nào NumPy giúp tăng performance đáng kể?
NumPy lưu dữ liệu trong memory như thế nào?
Sự khác nhau giữa np.array() và np.asarray() là gì?
Làm sao tính toán nhanh trên một mảng lớn trong NumPy?
Boolean indexing trong NumPy là gì?
NumPy thường được dùng chung với thư viện nào trong data pipeline?
Khi nào không nên dùng NumPy?
Goroutine hoạt động như thế nào?
Channel là gì? Blocking vs non-blocking?
So sánh concurrency model Go vs Python.
Context trong Go dùng để làm gì?
Memory management trong Go ra sao?
Làm sao implement graceful shutdown trong Gin?
Race condition là gì? Cách detect?
Struct embedding vs inheritance.
Interface trong Go hoạt động thế nào?
Làm sao tối ưu performance API Go?


# III. Database Design & Optimization
Multi-tenant architecture nên thiết kế database như thế nào?
Làm sao viết test không phụ thuộc database thật?
Index hoạt động thế nào trong PostgreSQL?
Khi nào index làm chậm hệ thống?
Explain Analyze dùng để làm gì?
Isolation level gồm những gì?
Deadlock xảy ra khi nào?
Phân biệt optimistic vs pessimistic locking.
Transaction ACID là gì?
Partitioning trong PostgreSQL dùng khi nào?
So sánh Redis vs Memcached.
Redis Cluster và Redis Sentinel
Cache invalidation strategies?
N+1 query problem là gì?
Thiết kế schema thế nào để tránh N+1 query?
Khi nào dùng NoSQL như DynamoDB?
Cách thiết kế schema cho multi-tenant.
Replication trong PostgreSQL hoạt động thế nào?
Connection pool là gì? Tại sao quan trọng?
Seq Scan vs Index Scan khác nhau thế nào và khi nào Seq Scan lại nhanh hơn?
Index B-tree, Hash, GIN, GiST khác nhau thế nào và dùng khi nào?
Index có giúp cho LIKE hoặc ILIKE không?
Khi nào PostgreSQL không sử dụng index dù đã tạo?
Batch insert vs single insert khác nhau thế nào?
Làm sao tối ưu insert/update hàng loạt(bulk operation)?
Khi nào transaction quá dài gây vấn đề?
Lock và blocking ảnh hưởng performance ra sao?
Cách kiểm tra query đang bị lock?
Khi nào nên dùng composite index và thứ tự cột trong index quan trọng ra sao?
Covering index(index only scan) là gì?
Bitmap Index Scan dùng khi nào?
Subquery vs JOIN khác nhau về hiệu năng ra sao?
Làm sao tối ưu truy vấn có ORDER BY và LIMIT?
Làm sao tối ưu truy vấn có GROUP BY và aggregation lớn?
Window function ảnh hưởng hiệu năng thế nào?
Bạn hiểu thế nào về query planner và cost-based optimizer trong PostgreSQL?
Statistics(ANALYZE) ảnh hưởng thế nào đến execution plan?
Cách đọc execution plan để tìm bottleneck?
Làm sao phát hiện slow query trong production(pg_stat_statements, log_min_duration_statement)?
Tại sao thiếu index có thể gây high CPU?
Khi nào cần tăng work_mem hoặc shared_buffers?
Khi nào cần connection pool như PgBouncer?
Cách tối ưu connection cho workload cao?
Autovacuum hoạt động ra sao và khi nào cần tuning?
Khi nào cần VACUUM và VACUUM FULL?
CTE(WITH) ảnh hưởng thế nào đến performance ở các version PostgreSQL mới?
Khi nào nên dùng materialized view?
Khi nào nên denormalize để tăng hiệu năng?
Khi nào cần full-text search với GIN index?
Làm sao tối ưu truy vấn có JOIN nhiều bảng lớn?
Khi nào nên dùng partitioning để tăng hiệu năng truy vấn?
Partition pruning hoạt động thế nào?
Parallel query trong PostgreSQL hoạt động ra sao?
Khi nào replication có thể ảnh hưởng read performance?
Hard parse vs soft parse
Khi nào dùng DynamoDB thay vì RDS?
DynamoDB vs OpenSearch


# IV. Microservices & System Design
So sánh monolith vs microservices. Khi nào KHÔNG nên dùng microservices?
Trong project Lodging Transport(event-driven), bạn sẽ thiết kế communication giữa các service như thế nào?
Phân biệt synchronous(REST) vs asynchronous(message queue). Trade-off?
Làm sao để tránh tight coupling giữa các microservices?
Thiết kế API Gateway cho hệ thống banking multi-core.
Thiết kế hệ thống có thể scale từ 1 instance lên 100 instance.
Làm sao để đảm bảo backward compatibility khi thay đổi API?
API Gateway pattern giải quyết vấn đề gì trong microservices?
Strangler Fig pattern dùng khi migrate từ monolith sang microservices ra sao?


# V. Distributed Systems & Transactions
Làm sao để xử lý distributed transaction? So sánh 2PC vs Saga pattern.
Circuit Breaker là gì? Khi nào cần?
Idempotency trong API là gì? Áp dụng vào payment/booking như thế nào?
Nếu một service downstream bị chậm, hệ thống sẽ bị ảnh hưởng ra sao? Cách mitigate?
Idempotency Key vs Trace ID
Observer pattern hoạt động thế nào trong event-driven system?
Unit of Work pattern giải quyết vấn đề gì trong transaction?
CQRS pattern là gì và khi nào nên dùng?
Saga pattern giúp quản lý distributed transaction như thế nào?
Circuit Breaker pattern là gì và giúp hệ thống resilient ra sao?
Retry pattern nên dùng khi nào và có rủi ro gì?
Bulkhead pattern giúp tránh cascading failure như thế nào?
Event Sourcing pattern là gì?
Outbox pattern giúp đảm bảo consistency giữa database và message queue như thế nào?
Làm sao implement retry logic và exponential backoff?
Circuit breaker pattern trong Python làm thế nào?
CAP theorem là gì?
Eventual consistency là gì?
Message ordering trong Kafka đảm bảo như thế nào?
Exactly-once semantics có thật sự tồn tại không?
Backpressure là gì?
Leader election trong distributed system.
Data sharding là gì?
Clock skew ảnh hưởng thế nào?
IBM MQ vs Kafka
Luồng giao dịch kết hợp giữa Core Banking, IBM MQ và Kafka


# VI. Containerization & Orchestration
Service discovery trong Kubernetes hoạt động ra sao?
Multi-stage build là gì?
Cách tối ưu Docker image cho production?
Layer caching hoạt động ra sao?
ENTRYPOINT vs CMD khác nhau thế nào?
Docker networking gồm những loại nào?
Làm sao giảm size image Python?
Volume vs bind mount?
Healthcheck trong Docker dùng để làm gì?
Làm sao debug container production?
Pod là gì?
Deployment vs StatefulSet.
HPA(Horizontal Pod Autoscaler) hoạt động thế nào?
Làm sao scale down an toàn?
Liveness vs Readiness probe.
Service types trong K8s.
Ingress hoạt động ra sao?
Rolling update trong K8s.
Resource requests & limits.
CrashLoopBackOff là gì?
Tại sao pod bị OOMKilled?
Cách implement zero-downtime deployment.
Kubernetes autoscaling dựa vào metric nào?
Làm sao monitor cluster?


# VII. Cloud & Infrastructure
Blue-green vs Canary deployment khác nhau thế nào?
Cách quản lý configuration theo môi trường(dev/staging/prod)?
Load balancing L4 vs L7 khác nhau thế nào?
Horizontal scaling vs vertical scaling.
EC2 vs Lambda.
SQS vs SNS.
Làm sao thiết kế system HA trên AWS?
Auto Scaling Group hoạt động ra sao?
VPC là gì?
Làm sao thiết kế hệ thống chịu được AZ failure?
Nếu migrate hệ thống on-premise lên AWS, bạn sẽ làm gì đầu tiên?


# VIII. Security
Authentication và Authorization khác nhau thế nào?
JWT là gì và nó hoạt động ra sao?
JWT gồm những phần nào(header, payload, signature)?
JWT có những rủi ro bảo mật nào?
Khi nào nên dùng JWT vs session-based authentication?
Access token và Refresh token khác nhau thế nào?
Tại sao access token nên có expiration time ngắn?
Làm sao revoke JWT khi user logout?
OAuth 2.0 là gì? Nó giải quyết vấn đề gì?
Các flow phổ biến của OAuth2 là gì?
OAuth2 vs OpenID Connect khác nhau thế nào?
Khi nào nên dùng API key authentication?
Rate limiting là gì và tại sao cần nó?
Các thuật toán rate limiting phổ biến là gì?
Rate limiting nên đặt ở API Gateway hay service level?
Throttling vs rate limiting khác nhau thế nào?
Blacklist và Whitelist là gì?
Khi nào nên dùng IP whitelist?
Làm sao bảo vệ API khỏi brute-force attack?
Làm sao bảo vệ API khỏi credential stuffing?
SQL Injection là gì và cách phòng tránh?
XSS(Cross-site scripting) là gì?
CSRF attack là gì và cách phòng tránh?
Tại sao cần HTTPS / TLS cho API?
CORS là gì và tại sao cần nó?
SameSite cookie giúp chống CSRF như thế nào?
Tại sao JWT không nên chứa dữ liệu nhạy cảm?
JWT nên lưu ở đâu? Cookie vs LocalStorage
Tại sao refresh token nên lưu an toàn hơn access token?
Token rotation là gì?
Làm sao phát hiện token replay attack?
Làm sao authenticate giữa các microservices?
mTLS(mutual TLS) là gì?
Service mesh giúp bảo mật microservices như thế nào?
Secret management nên làm thế nào trong production?
Tại sao không nên lưu secret trong source code?
IAM role vs IAM user trong AWS khác nhau thế nào?
Principle of least privilege là gì?
Làm sao quản lý secrets trong Kubernetes?
Tại sao cần network policies trong Kubernetes?
AWS Security Group vs NACL khác nhau thế nào?
Làm sao bảo vệ S3 bucket khỏi public access?
Làm sao quản lý secrets an toàn trong Python app?
Security best practice khi build Docker image?
ConfigMap vs Secret trong Kubernetes.
IAM role hoạt động thế nào?


# IX. Observability & Monitoring
Prometheus thu thập metric từ microservices như thế nào?
Trong Kubernetes, Prometheus discover service để scrape metric bằng cách nào?
Grafana lấy dữ liệu từ Prometheus như thế nào để hiển thị dashboard?
Metric, log và trace khác nhau như thế nào trong monitoring system?
Trong một hệ thống banking transaction, bạn sẽ monitor những metric nào quan trọng?
Làm sao expose metric từ Golang service cho Prometheus?
Histogram và Counter trong Prometheus dùng khi nào?
Alerting trong Prometheus hoạt động như thế nào?
Grafana dashboard thường dùng để visualize những metric gì trong production?
Làm sao phát hiện một service bị chậm trong hệ thống microservices?
Monitoring Kafka hoặc IBM MQ nên theo dõi metric nào?
Làm sao debug khi transaction bị chậm trong hệ thống banking?
Pull model của Prometheus khác gì với push model?
Khi hệ thống scale nhiều instance(Kubernetes), Prometheus xử lý metric aggregation như thế nào?
Nếu dashboard Grafana hiển thị CPU tăng cao nhưng request không tăng, bạn sẽ điều tra gì?
Bạn có trực tiếp config Prometheus không?
Logging trong hệ thống microservices thường được thiết kế như thế nào?
Vai trò của từng thành phần trong EFK stack là gì?
Fluentd thu thập log từ Kubernetes pods như thế nào?
Tại sao Fluentd thường chạy dưới dạng DaemonSet trong Kubernetes?
Log từ container đi qua pipeline như thế nào trước khi lưu vào Elasticsearch?
Structured logging là gì? Tại sao nên dùng JSON log?
Trong một hệ thống banking transaction, log nên chứa những thông tin gì?
Làm sao tìm log của một request cụ thể trong hệ thống microservices?
Khi một service bị lỗi production, bạn debug bằng log như thế nào?
Index trong Elasticsearch là gì? Log được lưu như thế nào?
Log rotation và retention nên được thiết kế ra sao trong production?
Làm sao giảm kích thước log để tránh Elasticsearch quá tải?
Log level(INFO, WARN, ERROR, DEBUG) nên dùng khi nào?
Nếu Elasticsearch bị chậm hoặc disk gần đầy thì ảnh hưởng gì đến hệ thống logging?
Làm sao liên kết log với monitoring metrics để debug hệ thống?
CloudWatch dùng để làm gì?
Thiết kế hệ thống logging tập trung cho microservices.
Cách logging chuẩn trong production?
Structured logging là gì?


# X. Frontend – Reacts
Virtual DOM trong React là gì?
Cơ chế diffing(reconciliation) của React hoạt động như thế nào?
Sự khác biệt chính giữa Virtual DOM và DOM thật là gì?
Tại sao key lại quan trọng khi render danh sách trong React?
Nếu dùng index làm key trong list, sẽ gặp những vấn đề gì?
Ví dụ cụ thể về trường hợp key bị sai dẫn đến bug giao diện?
Controlled component trong React là gì?
Uncontrolled component là gì và cách sử dụng?
Khi nào nên dùng controlled component, khi nào nên dùng uncontrolled?
SyntheticEvent trong React là gì?
SyntheticEvent khác native DOM event ở những điểm nào?
Tại sao React cần dùng SyntheticEvent thay vì event native?
useEffect trong React hoạt động như thế nào?
Dependency array trong useEffect có vai trò gì?
Khi dependency array là[] thì useEffect chạy lúc nào?
Khi không truyền dependency array thì useEffect chạy ra sao?
Cleanup function trong useEffect dùng để làm gì?
Cho ví dụ thực tế về cleanup trong useEffect(subscription, timer…).
Tại sao cleanup chạy trước khi component unmount và trước khi effect chạy lại?
useMemo dùng để làm gì?
useCallback dùng để làm gì?
Điểm khác biệt chính giữa useMemo và useCallback?
Khi nào KHÔNG nên dùng useMemo hoặc useCallback?
React.memo là gì và hoạt động như thế nào?
React.memo khác useMemo ở điểm nào?
Khi nào nên dùng React.memo cho component?
Inline function hoặc object trong props gây re-render như thế nào?
Lifting state up là gì?
Props drilling là gì và tại sao nó gây khó chịu?
Khi nào nên dùng Context API thay vì chỉ truyền props?
useRef khác useState ở những điểm nào?
Khi nào nên dùng useRef thay vì useState để tránh re-render?
Batch update(automatic batching) trong React là gì?
React batch state updates khác nhau giữa event handler và async code như thế nào?
Concurrent Rendering trong React 18 là gì?
useTransition dùng để làm gì?
useTransition giúp cải thiện UX trong trường hợp nào?
StrictMode trong React dùng để làm gì?
Tại sao useEffect chạy 2 lần trong StrictMode(ở development)?
Suspense component hoạt động như thế nào?
Suspense có thể dùng cho data fetching không?
Error Boundary là gì và cách hoạt động?
Code splitting trong React làm như thế nào?
React.lazy và Suspense dùng để lazy-load component ra sao?
Portals trong React là gì?
Dùng Portal trong những trường hợp nào(ví dụ cụ thể)?
Tại sao Hooks không thể bắt error như Error Boundary trong class ?
Higher-Order Component(HOC) là gì?
Render Props pattern là gì?
So sánh HOC vs Render Props vs Custom Hooks?
Ưu nhược điểm chính của Hooks so với HOC và Render Props?
Làm sao detect re-render không cần thiết trong React?
Tại sao component re-render dù props không đổi?
Khi nào nên memoize(useMemo, useCallback, memo)?
Khi nào memoization trở thành over-optimization?
Debounce và Throttle trong React dùng để làm gì?
Virtualization(windowing) là gì?
Khi nào cần dùng virtualization(ví dụ danh sách 10k items)?
Cách phổ biến để tối ưu bundle size trong React app?
Redux hoạt động theo ba nguyên lý chính nào?
Flow dữ liệu cơ bản trong Redux: dispatch → reducer → store?
Tại sao reducer phải là pure function?
Immutability quan trọng như thế nào trong Redux?
Single source of truth trong Redux mang lại lợi ích gì?
Tại sao không nên lưu derived state(state tính toán được) trong store?
Redux khác Context API ở những điểm chính nào?
Khi nào nên dùng Redux, khi nào chỉ cần Context + useReducer?
Redux Thunk và Redux Saga khác nhau cơ bản như thế nào?
Backend-for -Frontend(BFF) pattern dùng khi nào?
