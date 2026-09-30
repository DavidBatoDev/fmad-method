![FMAD — Foundry Method for Agile AI-Driven Development (phát triển phần mềm hướng AI theo lối agile)](banner-fmad-method.png)

[![Version](https://img.shields.io/github/v/tag/DavidBatoDev/fmad-method?color=e8702a&label=version)](https://github.com/DavidBatoDev/fmad-method/tags)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Docs](https://img.shields.io/badge/docs-GitHub%20Pages-1f2937)](https://davidbatodev.github.io/fmad-method/)

[English](README.md) | [简体中文](README_CN.md) | Tiếng Việt | [한국어](README_KR.md)

**FMAD — Foundry Method for Agile AI-Driven Development (phát triển phần mềm hướng AI theo lối agile). Biến một ý tưởng hoặc một yêu cầu thay đổi thành phần mềm chạy được mà không phải từ bỏ phần suy nghĩ.**

Phát triển hướng AI bao trùm toàn bộ công việc chứ không chỉ phần mã: xây dựng cái gì, các phần gắn kết với nhau ra sao, và thay đổi thế nào khi bạn hiểu thêm. Foundry Method là một cách làm điều đó theo lối agile. Quyết định luôn tường minh, ngữ cảnh được mang theo xuyên suốt, và quy trình tự co giãn theo khối lượng công việc. Thay đổi nhỏ đi thẳng vào khâu xây dựng. Công việc phức tạp được đầu tư đúng độ sâu cần thiết. Cùng một phương pháp dùng được cho cả nguyên mẫu hackathon lẫn hệ thống đã có nhiều năm lịch sử phía sau.

![Vòng lặp chuyển giao của FMAD: một ý niệm còn mơ hồ bắt đầu ở Clarify (Làm rõ), một ý tưởng lớn đã rõ ràng bắt đầu ở Plan (Lập kế hoạch), và một thay đổi nhỏ bắt đầu ở Build and verify (Xây dựng và kiểm chứng); Learn and adjust (Học hỏi và điều chỉnh) quay vòng trở lại Plan](docs/images/fmad-delivery-loop.svg)

_Bắt đầu từ bất kỳ đâu. Dùng FMAD từ đầu đến cuối, hoặc mang các bản brief, đặc tả và kiến trúc của nó vào quy trình chuyển giao hiện có của bạn._

## Bắt đầu xây dựng

Bạn cần một công cụ lập trình AI có hỗ trợ skill (Claude Code, Codex, Cursor và các công cụ khác), [uv](https://docs.astral.sh/uv/) cho việc thiết lập FMAD và chạy các script Python, cùng [Node.js và npm](https://nodejs.org) cộng với Git cho Skills CLI. Trong dự án của bạn, hãy chạy:

```bash
npx skills add DavidBatoDev/fmad-method
```

Chọn các skill và công cụ lập trình bạn muốn. Hãy chọn kèm `fmad` để thiết lập và nhận trợ giúp, cùng bản ghi mô-đun (module record) của mỗi mô-đun có skill bạn chọn: `fmod-method` và `fmod-core-tools`. Nếu muốn cài theo tên thay vì chọn từ danh sách, hãy liệt kê chúng cùng nhau:

```bash
npx skills add DavidBatoDev/fmad-method --skill fmad --skill fmod-core-tools --skill fmod-method --skill fmad-build
```

Mở công cụ lập trình của bạn trong dự án và yêu cầu skill `fmad` chạy `fmad setup`. Sau đó gọi `fmad-build` kèm theo điều bạn muốn thay đổi. Hãy hỏi `fmad` bất cứ khi nào bạn cần hướng dẫn về bước tiếp theo hoặc bước nào là tùy chọn.

**[Xây dựng dự án đầu tiên với FMAD →](https://davidbatodev.github.io/fmad-method/start/build-your-first-change/)**

**[Thêm FMAD vào một codebase có sẵn →](https://davidbatodev.github.io/fmad-method/existing-codebases/start-in-an-existing-codebase/)**

Hãy yêu cầu chạy `fmad status` để kiểm tra phiên bản và xem nên chạy gì tiếp theo. Hãy yêu cầu chạy `fmad setup` để cài đặt bản cập nhật: nó chạy `npx skills update`, sau đó làm mới dự án và dọn dẹp các skill đã được đổi tên hoặc đã bị gỡ bỏ.

## Vì sao chọn FMAD?

Các trợ lý lập trình làm tốt phần triển khai, nhưng chúng thường biến những giả định chưa được nói ra thành mã. FMAD giữ quyền kiểm soát trong tay bạn, trong khi các agent và workflow của nó làm cho những quyết định quan trọng trở nên tường minh và lưu giữ chúng làm ngữ cảnh cho phần việc tiếp theo.

- **Quy trình đúng quy mô** — Đi thẳng vào triển khai với những thay đổi rõ ràng, hoặc bổ sung khâu lập kế hoạch sâu hơn cho các sáng kiến lớn hơn.
- **Mã mới hoặc mã có sẵn** — Bắt đầu từ con số không, hoặc thiết lập ngữ cảnh đã được kiểm chứng cho một codebase bạn tiếp quản và làm việc dựa trên những gì thực sự có ở đó.
- **Ngữ cảnh bền vững** — Mang các quyết định về sản phẩm và kỹ thuật theo suốt quá trình thay vì phải giải thích lại trong mỗi cuộc trò chuyện.
- **Góc nhìn chuyên biệt** — Huy động chuyên môn về sản phẩm, kiến trúc, UX, phát triển và kiểm thử khi điều đó hữu ích.
- **Cộng tác có hướng dẫn** — Dùng các workflow có cấu trúc và các cuộc thảo luận nhiều agent mà vẫn giữ quyền phán đoán trong tay bạn.
- **Một lộ trình chuyển giao thống nhất** — Đi từ những suy nghĩ ban đầu, qua triển khai đã được review, đến điều chỉnh và rút kinh nghiệm.

[Xem một thay đổi cần lập kế hoạch đến mức nào →](https://davidbatodev.github.io/fmad-method/plan/choose-a-planning-path/)

## Đội ngũ Foundry

FMAD đi kèm hai mô-đun. `fmod-method` chứa các workflow chuyển giao, còn `fmod-core-tools` chứa hub `fmad` và các công cụ độc lập. Các agent có tên riêng mang một góc nhìn vào bất kỳ cuộc trò chuyện nào, từng agent một hoặc cùng nhau trong `fmad-party-mode`.

| Agent | Skill | Mang đến |
| --- | --- | --- |
| 📊 **Ember** — Chuyên viên phân tích nghiệp vụ | `fmad-agent-analyst` | Nghiên cứu thị trường và miền nghiệp vụ, khám phá ưu tiên bằng chứng |
| 📋 **Flint** — Quản lý sản phẩm | `fmad-agent-pm` | Jobs-to-be-done, yêu cầu, những câu hỏi "tại sao?" sắc bén |
| 🎨 **Sienna** — Nhà thiết kế UX | `fmad-agent-ux-designer` | Hành trình người dùng, thiết kế tương tác, màn hình trước khi có mã |
| 🏗️ **Ferris** — Kiến trúc sư hệ thống | `fmad-agent-architect` | Công nghệ "nhàm chán" có chủ đích, các đánh đổi, những gì sẽ hỏng khi mở rộng quy mô |
| 💻 **Cinder** — Kỹ sư phần mềm cấp cao | `fmad-agent-dev` | Triển khai theo hướng test-first, ngắn gọn như một commit message |

Các workflow đảm nhận phần còn lại của vòng lặp: `fmad-brainstorming`, `fmad-forge-idea`, `fmad-product-brief`, `fmad-prfaq`, `fmad-deep-recon`, `fmad-prd`, `fmad-ux`, `fmad-architecture`, `fmad-spec`, `fmad-ticket`, `fmad-build`, `fmad-build-auto`, `fmad-code-review`, `fmad-review`, `fmad-walkthrough`, `fmad-qa-generate-e2e-tests`, `fmad-correct-course`, `fmad-retrospective`, `fmad-project-context`, `fmad-customize` và `fmad-advanced-elicitation`. Xem [tài liệu tham chiếu về skill và agent](https://davidbatodev.github.io/fmad-method/reference/skills-and-agents/).

## Lập kế hoạch trên web

Các [web bundle](web-bundles/) đóng gói một số workflow FMAD được chọn lọc thành Google Gemini Gems và ChatGPT Custom GPTs. Hãy dùng chúng để lập kế hoạch ngay trong gói đăng ký web bạn đang có, sau đó mang các artifact thu được vào công cụ lập trình AI của bạn để triển khai. Các bundle dạng nén zip được đính kèm trong các [bản phát hành](https://github.com/DavidBatoDev/fmad-method/releases).

## Tài liệu

- **[Xây dựng thay đổi đầu tiên](https://davidbatodev.github.io/fmad-method/start/build-your-first-change/)** — Cài đặt FMAD và xây dựng một dự án nhỏ.
- **[Chọn lộ trình lập kế hoạch](https://davidbatodev.github.io/fmad-method/plan/choose-a-planning-path/)** — Chọn mức độ lập kế hoạch mà một thay đổi cần và xem mỗi skill lập kế hoạch tạo ra những gì.
- **[Bắt đầu trong một codebase có sẵn](https://davidbatodev.github.io/fmad-method/existing-codebases/start-in-an-existing-codebase/)** — Thêm FMAD vào một codebase có sẵn.

## Góp ý

FMAD là bộ công cụ cá nhân dành cho các dự án và hackathon của riêng tôi, được chia sẻ với hy vọng nó cũng giúp ích cho bạn.

- [GitHub Issues](https://github.com/DavidBatoDev/fmad-method/issues) — Báo lỗi và đề xuất tính năng.
- [GitHub Discussions](https://github.com/DavidBatoDev/fmad-method/discussions) — Đặt câu hỏi và chia sẻ ý tưởng.

Hãy đọc [CONTRIBUTING.md](CONTRIBUTING.md) trước khi mở pull request.

## Lời cảm ơn

FMAD được lấy cảm hứng rất nhiều từ [BMAD-METHOD™](https://github.com/bmad-code-org/BMAD-METHOD) của BMad Code, LLC và là sản phẩm phái sinh từ dự án đó; BMAD-METHOD™ được phát hành theo Giấy phép MIT. FMAD đổi tên các skill, mô-đun và persona, đồng thời thay đổi nhận diện thương hiệu, nhưng phương pháp, các workflow và một phần lớn văn bản đều đến từ dự án đó. Công lao đối với những ý tưởng nền tảng thuộc về các tác giả và những người đóng góp của dự án đó. Xem [NOTICE.md](NOTICE.md) để biết chi tiết.

FMAD là một dự án độc lập. FMAD không có quan hệ liên kết với BMad Code, LLC, và cũng không được BMad Code, LLC xác nhận (bảo chứng) hay tài trợ. BMad™, BMad Method™ và BMAD-METHOD™ là các nhãn hiệu của BMad Code, LLC.

## Giấy phép

Giấy phép MIT. Xem [LICENSE](LICENSE) để biết chi tiết.
