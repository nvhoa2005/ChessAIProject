# Bài tập lớn môn Trí tuệ Nhân tạo - INT3401E 5, Nhóm 2
## 1. Giới thiệu Team
- Trịnh Hải Tiến    - 23021697
- Nguyễn Văn Hòa    - 23021556
- Cao Vũ Nhật Triều - 23021740

## 2. Demo dự án 
https://www.youtube.com/watch?v=rc-csaTpUyk

## 3. Ý tưởng của dự án.

- Dự án hướng đến việc xây dựng một chess engine với mức elo ~ 2200, có thể đưa ra các nước đi chính xác và cạnh tranh tốt với người chơi có trình độ. Ý tưởng trọng tâm là tái hiện một AI chơi cờ cổ điển hiệu quả cao như trong các engine nổi tiếng (ví dụ: Stockfish), nhưng giới hạn trong phạm vi hiểu biết của sinh viên mới tiếp cận đến trí tuệ nhân tạo.
Thay vì dùng học máy hoặc các phương pháp học sâu, engine áp dụng các thuật toán truyền thống đã được chứng minh hiệu quả trong AI chơi cờ.
- Dùng bitboard để biểu diễn bàn cờ, giúp thao tác nhanh chóng trên từng ô cờ bằng toán tử bit.
- Kết hợp các chiến lược tìm kiếm thông minh như Alpha-Beta pruning, Iterative Deepening, Quiescence Search, và ghi nhớ trạng thái thông qua Transposition Table với Zobrist Hashing.
- Mục tiêu của thiết kế là tạo một hệ thống:
- Nhanh: có thể phản hồi trong vài giây (dưới 10 giây).
- Chính xác: không phạm luật, biết xử lý các trường hợp đặc biệt (phong cấp, enpassant,…).
- Mở rộng dễ dàng: cho phép kết hợp với GUI hoặc AI học máy trong tương lai.

## 4. Các thuật toán chính

### 4.1.	Alphan-Beta Pruning (Tối ưu Minimax)
- Là nền tảng chính để tìm kiếm nước đi tối ưu.
- Được áp dụng dưới dạng Negamax để đơn giản hóa mã nguồn.
- Cắt tỉa các nhánh không cần thiết nếu:
- Một nước đi đã vượt qua beta (không cần xét nước còn lại).
- Kết quả: giúp giảm đáng kể số lượng node cần duyệt, đặc biệt khi kết hợp với sắp xếp nước đi tốt.

### 4.2. Iterative Deepening
- Thay vì tìm trực tiếp đến độ sâu cố định thì engine sẽ tìm dần từ depth bằng 1 đến 2 đến 3 đến …. Lợi ích:
- Có thể dừng sớm khi hết thời gian, luôn có một “best move” tạm thời.
- Kết hợp tốt với Transposition Table: các node ở độ sâu thấp được lưu sẵn, dùng lại cho các độ sâu cao hơn.
- Cải thiện chất lượng sắp xếp nước đi, giúp Alpha-Beta hoạt động hiệu quả hơn.

### 4.3. Quiescence Search
- Khi đạt depth bằng 0, engine không đánh giá ngay, mà mở rộng tiếp các nước ăn quân.
- Mục tiêu: tránh đánh giá sai trong các trạng thái không ổn định (ví dụ đang bị ăn quân).
- Chỉ dừng khi trạng thái bàn cờ “ổn định” (không còn ăn quân khả thi).

### 4.4. Transposition Table và Zobrist Hashing
- Zobrist Hashing mã hóa toàn bộ trạng thái bàn cờ thành một số 64-bit duy nhất.
- Transposition Table lưu các trạng thái đã duyệt gồm:
- Giá trị đánh giá.
- Độ sâu.
- Nước đi tốt nhất đã duyệt (hash move).
- Nếu gặp lại trạng thái cũ (qua đường đi khác), engine có thể:
- Dùng lại kết quả ➜ tiết kiệm thời gian.
- Cắt tỉa sớm hơn trong Alpha-Beta.

## 5. Evaluation – các phép tính đánh giá trạng thái bàn cờ
Việc đánh giá trạng thái bàn cờ là tâm điểm của engine, quyết định chất lượng nước đi.

### 5.1. Tổng điểm đánh giá
- Giá trị đánh giá được tính theo công thức:

  ### Eval = (giá trị trắng) – (giá trị đen)

- Trong đó, mỗi bên gồm 3 thành phần chính: Giá trị quân (Material); Vị trí trên bàn cờ (Piece-square table); Tàn cuộc (Endgame heuristics).

### 5.2. Giá trị quân
- Pawn: 100
- Knight: 300
- Bishop: 320
- Rook: 500
- Queen: 900
- King: vô hạn (chỉ đánh giá qua vị trí)
- Giá trị này dùng để xác định lợi thế vật chất.

### 5.3. Piece-Square Table
- Mỗi loại quân có bảng 64 ô đánh giá vị trí cụ thể.
- Ví dụ: Tốt ở trung tâm có điểm cao hơn ở biên. Mã ở gần trung tâm linh hoạt hơn. Vua trong tàn cuộc nên ra giữa, còn ở khai cuộc nên giữ gần góc.
- Điều này giúp engine đánh giá không chỉ số lượng quân, mà còn thế đứng chiến lược.

### 5.4. Mop-Up Evaluation (Tàn cuộc)
- Khi bên mình hơn quân rõ rệt, engine ưu tiên đẩy vua đối phương về góc bàn.
- Tính toán bằng:
- Khoảng cách Manhattan từ vua địch đến trung tâm (Khoảng cách Manhattan là một cách đo khoảng cách giữa hai điểm trên lưới (grid), chỉ cho phép di chuyển theo chiều ngang và dọc)
- Số nước đi xe có thể bắt được vua địch.
- Hiệu quả trong việc chiếu hết nhanh chóng và tránh bị hòa trong tàn cuộc.

## 6. Đánh giá hiệu suất
### 6.1. Thời gian và tốc độ
- Trung bình mỗi nước đi 2 giây
- Dù thời gian ngắn, engine vẫn đảm bảo:
- Không bỏ sót nước đi quan trọng
- Biết phòng thủ trước các mối đe dọa (chiếu, ăn quân…)

### 6.2. Độ chính xác
- Không phạm luật trong các ván kiểm thử.
- Xử lý đúng các luật đặc biệt:
- Nhập thành, En Passant, phong cấp, hòa do lặp lại,…
- Biết chiếu hết, chống chiếu, xử lý quân bị ghim.

### 6.3. So sánh thực tế
Elo ~ 2200, xem dữ liệu đo đạc ghi nhận qua khoảng 20 trận đấu trong github ở trên.
