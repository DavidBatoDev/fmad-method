---
title: "Cách tìm câu trả lời về FMAD"
description: Sử dụng LLM để tự nhanh chóng trả lời các câu hỏi về FMAD
sidebar:
        order: 4
---

Hãy dùng trợ giúp tích hợp sẵn của FMAD, tài liệu nguồn, hoặc cộng đồng để tìm câu trả lời, theo thứ tự từ nhanh nhất đến đầy đủ nhất.

## 1. Hỏi FMAD-Help

Cách nhanh nhất để có câu trả lời. Skill `fmad-help` có sẵn ngay trong phiên AI của bạn và xử lý được hơn 80% câu hỏi. Nó sẽ kiểm tra dự án, nhìn xem bạn đã hoàn thành đến đâu và cho bạn biết nên làm gì tiếp theo.

```text
fmad-help Tôi có ý tưởng SaaS và đã biết tất cả tính năng. Tôi nên bắt đầu từ đâu?
fmad-help Tôi có những lựa chọn nào cho thiết kế UX?
fmad-help Tôi đang bị mắc ở workflow PRD
```

:::tip
Bạn cũng có thể dùng `/fmad-help` hoặc `$fmad-help` tùy nền tảng, nhưng chỉ `fmad-help` là cách nên hoạt động mọi nơi.
:::

## 2. Đi sâu hơn với mã nguồn

FMAD-Help dựa trên cấu hình bạn đã cài đặt. Nếu bạn cần tìm hiểu nội bộ, lịch sử, hay kiến trúc của FMAD, hoặc đang nghiên cứu FMAD trước khi cài, hãy để AI đọc trực tiếp mã nguồn.

Hãy clone hoặc mở [repo FMAD-METHOD](https://github.com/DavidBatoDev/fmad-method) rồi hỏi AI của bạn về nó. Bất kỳ công cụ nào có hỗ trợ agent như Claude Code, Cursor, Windsurf... đều có thể đọc mã nguồn và trả lời trực tiếp.

:::note[Ví dụ]
**Q:** "Hãy chỉ tôi cách nhanh nhất để xây dựng một thứ gì đó bằng FMAD"

**A:** Chạy `fmad-build`. Đưa vào ý định trực tiếp, issue, spec hoặc story đã lập kế hoạch; workflow dùng ngữ cảnh sẵn có và chọn độ sâu làm rõ, lập kế hoạch, triển khai và review cần thiết.
:::

**Mẹo để có câu trả lời tốt hơn:**

- **Hãy hỏi thật cụ thể** - "Bước 3 trong workflow PRD làm gì?" sẽ tốt hơn "PRD hoạt động ra sao?"
- **Kiểm tra lại những câu trả lời nghe lạ** - LLM đôi khi vẫn sai. Hãy kiểm tra file nguồn hoặc hỏi trên [GitHub Discussions](https://github.com/DavidBatoDev/fmad-method/discussions).

### Không dùng agent? Dùng trang docs

Nếu AI của bạn không đọc được file cục bộ như ChatGPT hoặc Claude.ai, hãy mở [trang tài liệu FMAD](https://davidbatodev.github.io/fmad-method/).

## 3. Hỏi người thật

Nếu cả FMAD-Help lẫn mã nguồn vẫn chưa trả lời được câu hỏi của bạn, lúc này bạn đã có một câu hỏi rõ hơn nhiều để đem đi hỏi cộng đồng.

| Kênh | Dùng cho |
| --- | --- |
| GitHub Discussions | Câu hỏi, ý tưởng và đề xuất tính năng |
| GitHub Issues | Báo lỗi |

**GitHub Discussions:** [github.com/DavidBatoDev/fmad-method/discussions](https://github.com/DavidBatoDev/fmad-method/discussions)

**GitHub Issues:** [github.com/DavidBatoDev/fmad-method/issues](https://github.com/DavidBatoDev/fmad-method/issues)

*Chính bạn,*
        *đang mắc kẹt*
             *trong hàng đợi -*
                      *đợi*
                              *ai?*

*Mã nguồn*
        *nằm ngay đó,*
                *rõ như ban ngày!*

*Hãy trỏ*
        *cho máy của bạn.*
                    *Thả nó đi.*

*Nó đọc.*
        *Nó nói.*
                *Cứ hỏi -*

*Sao phải chờ*
        *đến ngày mai*
                *khi bạn đã có*
                        *ngày hôm nay?*

*- Claude*
