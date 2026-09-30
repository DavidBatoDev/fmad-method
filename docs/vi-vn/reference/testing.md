---
title: Kiểm Thử
description: Workflow QA tích hợp sẵn cho tự động hóa kiểm thử.
sidebar:
  order: 6
---

FMAD cung cấp workflow QA tích hợp sẵn để tạo test nhanh cho dự án của bạn.

## Workflow QA Tích Hợp Sẵn

Workflow QA tích hợp sẵn (`fmad-qa-generate-e2e-tests`) nằm trong module FMM (Agile suite), khả dụng thông qua Developer agent. Nó tạo test chạy được rất nhanh bằng framework kiểm thử hiện có của dự án, không cần thêm cấu hình hay bước cài đặt bổ sung.

**Trigger:** `QA` (thông qua Developer agent) hoặc `fmad-qa-generate-e2e-tests`

### Workflow Làm Gì

Workflow QA (Automate) gồm năm bước:

1. **Phát hiện framework test** — quét `package.json` và các file test hiện có để nhận ra framework của bạn như Jest, Vitest, Playwright, Cypress hoặc bất kỳ runner tiêu chuẩn nào. Nếu chưa có gì, nó sẽ phân tích stack dự án và đề xuất một lựa chọn.
2. **Xác định tính năng** — hỏi cần kiểm thử phần nào hoặc tự khám phá các tính năng trong codebase.
3. **Tạo API tests** — bao phủ status code, cấu trúc phản hồi, happy path và 1-2 trường hợp lỗi.
4. **Tạo E2E tests** — bao phủ workflow người dùng bằng semantic locator và assertion trên kết quả nhìn thấy được.
5. **Chạy và xác minh** — thực thi test vừa tạo và sửa lỗi hỏng ngay lập tức.

Workflow tạo một bản tóm tắt kiểm thử và lưu nó vào thư mục implementation artifacts của dự án.

### Mẫu Kiểm Thử

Các test được tạo theo triết lý “đơn giản và dễ bảo trì”:

- **Chỉ dùng API chuẩn của framework** — không kéo thêm utility ngoài hay abstraction tùy chỉnh
- **Semantic locator** cho UI test — dùng role, label, text thay vì CSS selector
- **Test độc lập** — không phụ thuộc thứ tự chạy
- **Không hardcode wait hoặc sleep**
- **Mô tả rõ ràng** để test cũng đóng vai trò tài liệu tính năng

:::note[Phạm vi]
Workflow QA chỉ tạo test. Nếu bạn cần code review hoặc xác nhận story, hãy dùng workflow Code Review (`CR`).
:::

### Khi Nào Nên Dùng QA Tích Hợp S���n

- Cần bao phủ test nhanh cho một tính năng mới hoặc hiện có
- Muốn tự động hóa kiểm thử thân thiện với người mới mà không cần thiết lập phức tạp
- Muốn các pattern test chuẩn mà lập trình viên nào cũng đọc và bảo trì được
- Dự án nhỏ-trung bình, nơi chiến lược kiểm thử toàn diện là không cần thiết

## Kiểm Thử Nằm Ở Đâu Trong Workflow

Workflow QA Automate xuất hiện ở Phase 4 (Implementation) trong workflow map của Foundry Method. Nó được thiết kế để chạy **sau khi hoàn tất trọn vẹn một epic** — tức là khi mọi story trong epic đó đã được triển khai và code review xong. Trình tự điển hình là:

1. Với mỗi story trong epic: triển khai bằng Build (`BD` / `fmad-build`), sau đó thêm Code Review (`CR`) khi cần
2. Sau khi epic hoàn tất: tạo test bằng `QA` (thông qua Developer agent)
3. Chạy retrospective (`fmad-retrospective`) để ghi nhận bài học rút ra

Workflow QA tích hợp sẵn làm việc trực tiếp từ source code mà không cần nạp tài liệu lập kế hoạch như PRD hay architecture.

Để hiểu rõ hơn kiểm thử nằm ở đâu trong quy trình tổng thể, xem [Workflow Map](./workflow-map.md).
