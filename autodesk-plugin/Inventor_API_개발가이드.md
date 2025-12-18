# Autodesk Inventor 2026 API 개발 가이드

## 목차
1. [개요](#개요)
2. [C# 개발환경 설정](#c-개발환경-설정)
3. [Python 개발환경 설정](#python-개발환경-설정)
4. [Visual Studio 2026 호환성 문제](#visual-studio-2026-호환성-문제)
5. [참조 자료](#참조-자료)

---

## 개요

Autodesk Inventor 2026은 COM 기반 API를 제공하며, 다양한 프로그래밍 언어를 통해 자동화 및 커스터마이징이 가능합니다.

### 지원 언어
- C# (공식 지원)
- Visual Basic (공식 지원)
- C++ (공식 지원)
- Python (COM을 통한 지원)
- Java (COM을 통한 지원)

### 주요 리소스 위치
- **SDK 위치**: `C:\Users\Public\Documents\Autodesk\Inventor 2026\SDK\`
- **Public Assemblies**: `C:\Program Files\Autodesk\Inventor 2026\Bin\Public Assemblies\`
- **API 도움말**: SDK 폴더 내 또는 온라인

---

## C# 개발환경 설정

### 1. 사전 준비

#### 필수 소프트웨어
- **Autodesk Inventor 2026**: 필수
- **Visual Studio 2022 (v17.8 이상)**: 공식 지원 버전
  - Professional 에디션 권장
  - Community 에디션도 사용 가능
- **.NET 8**: Inventor 2025+ 버전부터 필요
  - 이전 버전(2024 이하)은 .NET Framework 4.8 사용
- **워크로드**: ".NET desktop development" 포함

### 2. Inventor SDK Developer Tools 설치

1. SDK 폴더로 이동:
   ```
   C:\Users\Public\Documents\Autodesk\Inventor 2026\SDK\
   ```

2. `DeveloperTools.msi` 실행
   - Visual Studio용 Inventor 애드인 템플릿 자동 설치
   - **주의**: Visual Studio 2022만 공식 지원

### 3. Visual Studio 프로젝트 생성

1. Visual Studio 2022 실행
2. "새 프로젝트 만들기" 선택
3. "Autodesk Inventor AddIn" 템플릿 검색
4. C# 템플릿 선택
5. 프로젝트 설정:
   - **프로젝트 타입**: Class Library
   - **Target Framework**: .NET 8

### 4. 프로젝트 참조 설정

#### DLL 참조 추가
1. 솔루션 탐색기에서 프로젝트 우클릭 → "추가" → "참조"
2. 다음 DLL 추가:
   ```
   C:\Program Files\Autodesk\Inventor 2026\Bin\Public Assemblies\Autodesk.Inventor.Interop.dll
   ```
3. 참조 속성 설정:
   - **Embed Interop Types**: `False`
   - **Copy Local**: `True`

#### 빌드 출력 경로 설정
```
C:\ProgramData\Autodesk\Inventor Addins\[프로젝트명]\
```

### 5. .addin 파일 생성

프로젝트에 `[프로젝트명].addin` XML 파일 추가:

```xml
<?xml version="1.0" encoding="utf-8"?>
<AddIn Type="Standard">
    <ClassId>{YOUR_GENERATED_GUID}</ClassId>
    <ClientId>{YOUR_GENERATED_GUID}</ClientId>
    <DisplayName>My Inventor Add-in</DisplayName>
    <Description>My first Inventor add-in</Description>
    <Assembly>YourAddinName.dll</Assembly>
    <SiteFolder/>
    <Version>1.0.0.0</Version>
    <SupportedSoftwareVersionGreaterThan>30.0</SupportedSoftwareVersionGreaterThan>
    <Data/>
</AddIn>
```

**GUID 생성 방법**:
- Visual Studio: "도구" → "GUID 만들기"
- ClassId와 ClientId에 동일한 GUID 사용

**파일 속성 설정**:
- "출력 디렉터리에 복사": "새 버전이면 복사"

### 6. 기본 코드 구현

```csharp
using System.Runtime.InteropServices;
using Inventor;

namespace YourAddinNamespace
{
    [ProgId("YourAddinNamespace.StandardAddInServer")]
    [Guid("YOUR_GENERATED_GUID_HERE")] // .addin 파일과 동일한 GUID
    public class StandardAddInServer : ApplicationAddInServer
    {
        private Inventor.Application m_inventorApp;

        // Inventor 시작 시 호출
        public void Activate(ApplicationAddInSite addInSiteObject, bool firstTime)
        {
            m_inventorApp = addInSiteObject.Application;

            // 초기화 코드 작성
            System.Windows.Forms.MessageBox.Show("Add-in Loaded!");
        }

        // Inventor 종료 시 호출
        public void Deactivate()
        {
            // 리소스 정리
            m_inventorApp = null;
            System.GC.Collect();
            System.GC.WaitForPendingFinalizers();
        }

        public void ExecuteCommand(int commandID)
        {
            // 커스텀 명령 처리
        }

        public object Automation
        {
            get { return null; }
        }
    }
}
```

### 7. 디버깅 설정

1. 프로젝트 속성 → "디버그" 탭
2. "시작 외부 프로그램" 선택
3. Inventor 실행 파일 경로 지정:
   ```
   C:\Program Files\Autodesk\Inventor 2026\Bin\Inventor.exe
   ```

### 8. 빌드 및 테스트

1. **프로젝트 빌드**: `Ctrl + Shift + B`
2. **디버깅 시작**: `F5` → Inventor 자동 실행
3. Inventor에서 애드인 활성화:
   - "도구" 탭 → "옵션" → "Add-Ins"
   - 애드인 찾기
   - **"차단(Block)" 체크 해제**
   - "자동으로 로드" 및 "로드됨" 체크

### 주의사항

- GUID는 .addin 파일과 C# 코드에서 일치해야 함
- .dll과 .addin 파일이 같은 출력 폴더에 있어야 함
- Inventor 2026은 .NET 8 필수

---

## Python 개발환경 설정

Python으로 Inventor API를 사용하는 두 가지 방법이 있습니다.

### 방법 1: pywin32 COM 자동화 (기본 방법)

#### 설치

1. **Python 설치**
   - Python 3.x (Anaconda 배포판 권장)
   - Windows 전용 (Inventor는 Windows만 지원)

2. **pywin32 설치**
   ```bash
   pip install pywin32
   ```

#### 기본 사용 예제

```python
import win32com.client

# Inventor 애플리케이션에 연결
inventor = win32com.client.Dispatch("Inventor.Application")
inventor.Visible = True

# 기존 문서 열기 또는 새 문서 생성
part_doc = inventor.Documents.Add(
    win32com.client.constants.kPartDocumentObject
)

# 트랜잭션 객체 가져오기
trans_geom = inventor.TransientGeometry

# 스케치 생성 예제
comp_def = part_doc.ComponentDefinition
sketch = comp_def.Sketches.Add(comp_def.WorkPlanes.Item(1))

# 사용 가능한 메서드/속성 탐색
print(dir(inventor))
```

#### 장점
- 공식 Inventor API 직접 접근
- 모든 Inventor 기능 사용 가능
- C#/VBA 예제를 Python으로 변환 가능
- 타입 라이브러리 완전 지원

#### 단점
- COM API 이해 필요
- 타입 힌팅 제한적
- 코드가 다소 장황할 수 있음

### 방법 2: PyInventor 라이브러리 (추천)

#### 설치

```bash
# GitHub에서 클론
git clone https://github.com/AndrewOriani/PyInventor.git
cd PyInventor
python setup.py install

# 또는 pip으로 직접 설치
pip install git+https://github.com/AndrewOriani/PyInventor.git
```

#### 요구사항
- Python 3.x (Anaconda 권장)
- Inventor 2017 이상 (Inventor 2019 권장)
- Windows 전용
- 외부 의존성 없음 (Anaconda 배포판 사용 시)

#### 기본 사용 예제

```python
from PyInventor import pyinvent

# Inventor 애플리케이션 시작
inv = pyinvent.Inventor()

# 새 파트 생성
part = inv.create_part()

# PyInventor는 더 Python 친화적인 API 제공
# 자세한 내용은 GitHub 저장소의 튜토리얼 노트북 참조
```

#### 장점
- Python 친화적인 API
- 간단한 문법
- VBA 코드를 Python으로 래핑
- 튜토리얼 노트북 제공

#### 단점
- 서드파티 라이브러리
- 일부 고급 기능 제한적일 수 있음
- 공식 지원 없음

### 개발 환경 테스트

```python
import win32com.client

try:
    inventor = win32com.client.Dispatch("Inventor.Application")
    print(f"✓ Inventor 버전: {inventor.SoftwareVersion.DisplayVersion}")
    print(f"✓ 빌드 식별자: {inventor.SoftwareVersion.BuildIdentifier}")
    print(f"✓ Python-Inventor 연결 성공!")
except Exception as e:
    print(f"✗ 연결 실패: {e}")
```

### API 문서 위치
- **로컬**: `C:\Users\Public\Documents\Autodesk\Inventor 2026\Local Help`
- **온라인**: https://help.autodesk.com/view/INVNTOR/2022/ENU/

---

## Visual Studio 2026 호환성 문제

### 문제점

**DeveloperTools.msi가 Visual Studio 2026을 인식하지 못함**

- Visual Studio 2026이 2025년 11월에 정식 출시됨
- Autodesk Inventor 2026 SDK는 **Visual Studio 2022 (v17.8+)만 공식 지원**
- DeveloperTools.msi는 VS 2026을 감지하지 못하고 설치 실패

### 공식 지원 버전

**Autodesk Inventor 2026 SDK 공식 지원**:
- Visual Studio 2022 버전 17.8 이상
- .NET 8
- Visual Studio Professional 권장 (Community도 가능)

### 해결 방법

#### 방법 1: 수동 템플릿 설치 (가장 간단)

DeveloperTools.msi 없이 직접 템플릿 복사:

1. **템플릿 파일 찾기**:
   ```
   C:\Users\Public\Documents\Autodesk\Inventor 2026\SDK\
   ```
   이 폴더에서 `.zip` 형식의 템플릿 파일 찾기
   (예: `InventorAddinTemplate.zip`)

2. **Visual Studio 2026 템플릿 폴더로 복사**:
   ```
   C:\Users\[사용자이름]\Documents\Visual Studio 2026\Templates\ProjectTemplates\
   ```

3. **Visual Studio 2026 재시작**

4. **새 프로젝트 만들기**에서 "Inventor AddIn" 검색

#### 방법 2: Visual Studio 2022 병행 설치 (권장)

Visual Studio는 여러 버전을 동시에 설치할 수 있습니다:

1. **Visual Studio 2022 Community 다운로드**:
   https://visualstudio.microsoft.com/downloads/

2. **설치 시 워크로드 선택**:
   - ".NET desktop development" 체크

3. **DeveloperTools.msi 실행**:
   - VS 2022를 정상적으로 감지
   - 템플릿 자동 설치

4. **개발 방식**:
   - Inventor 애드인 개발: Visual Studio 2022 사용
   - 다른 프로젝트: Visual Studio 2026 계속 사용

#### 방법 3: Visual Studio 2019 경유 설치

1. Visual Studio 2019 Community 임시 설치
2. VS 2019를 한 번 실행하여 초기 설정
3. `DeveloperTools.msi` 실행 (VS 2019 감지됨)
4. 설치된 템플릿을 VS 2026 폴더로 수동 복사:
   ```
   복사 원본: %USERPROFILE%\Documents\Visual Studio 2019\Templates\ProjectTemplates\
   복사 대상: %USERPROFILE%\Documents\Visual Studio 2026\Templates\ProjectTemplates\
   ```
5. VS 2019는 제거 가능

#### 방법 4: 템플릿 없이 직접 프로젝트 구성

Visual Studio 2026에서 템플릿 없이 수동 설정:

1. **Class Library (.NET 8)** 프로젝트 생성
2. `Autodesk.Inventor.Interop.dll` 수동 참조 추가
3. `.addin` 파일 및 `StandardAddInServer.cs` 직접 작성
4. 빌드 출력 경로 및 디버깅 설정 수동 구성

### 권장 사항

현재 상황에서는 **방법 2 (VS 2022 병행 설치)**를 추천:
- Autodesk 공식 지원으로 안정성 보장
- 디버깅 및 개발 도구 완전 지원
- VS 2026도 계속 사용 가능
- 두 버전 간 충돌 없음

### SDK 지원 버전 확인 방법

SDK 폴더의 `SDK_Readme.htm` 파일 확인:
```
C:\Users\Public\Documents\Autodesk\Inventor 2026\SDK\SDK_Readme.htm
```

이 파일에 공식 지원 Visual Studio 버전 명시되어 있음.

---

## 참조 자료

### 공식 문서

1. **Autodesk Inventor API 개요**
   - https://help.autodesk.com/view/INVNTOR/2022/ENU/

2. **Inventor API 시작하기**
   - https://help.autodesk.com/view/INVNTOR/2022/ENU/?guid=GUID-4939ABD1-A15E-473E-9376-D8208EC029EB

3. **Autodesk Platform Services - Inventor API**
   - https://aps.autodesk.com/developer/overview/inventor

4. **Inventor 2026 시스템 요구사항**
   - https://www.autodesk.com/support/technical/article/caas/sfdcarticles/sfdcarticles/System-requirements-for-Autodesk-Inventor-2026.html

### C# 개발 리소스

5. **Visual Studio 2022 다운로드**
   - https://visualstudio.microsoft.com/downloads/

6. **Inventor Automation API Template (Visual Studio Marketplace)**
   - Visual Studio 2025+ 용 .NET 8 템플릿
   - https://marketplace.visualstudio.com/items?itemName=InventorAutomationAPITemplate

7. **ProtoTech 블로그 - C# API 커스터마이징**
   - https://www.prototechsolutions.com/blog/customizing-autodesk-inventor-using-api-in-csharp/

8. **Ketiv Technologies - Inventor Add-in 개발 가이드**
   - https://www.ketiv.com/learning/autodesk-inventor-addin-development-guide/

9. **Arkance - Inventor API 개발**
   - https://www.arkance.world/resources/inventor-api-development

### Python 개발 리소스

10. **PyInventor GitHub (AndrewOriani)**
    - Python 기반 Autodesk Inventor API 모듈
    - https://github.com/AndrewOriani/PyInventor

11. **PyInventor 문서**
    - https://thehubbit.github.io/PyInventor/

12. **PyInventor 설치 가이드**
    - https://github.com/TheHubbit/PyInventor/wiki/Installation

13. **Python과 Inventor - Autodesk 커뮤니티**
    - https://forums.autodesk.com/t5/inventor-customization/python-and-inventor/td-p/7875048

14. **pywin32를 사용한 Inventor COM API**
    - https://copyprogramming.com/howto/how-to-create-and-use-objects-from-the-inventor-com-api-in-python-pywin32

15. **Python으로 Inventor API 사용하기**
    - https://devcodef1.com/news/1003393/autodesk-inventor-2022-api-with-python

16. **Autodesk 커뮤니티 - Python으로 Inventor 작업하기**
    - https://forums.autodesk.com/t5/inventor-programming-ilogic/working-with-inventor-using-python/td-p/11824991

### Visual Studio 2026 관련

17. **Visual Studio 2026 릴리스 정보**
    - Visual Studio Magazine 기사
    - https://visualstudiomagazine.com/articles/2025/11/visual-studio-2026-ga.aspx

18. **Visual Studio 2026 다운로드 (Insiders)**
    - https://www.microsoft.com/en-us/download/visual-studio-2026

19. **Visual Studio 2026 출시 발표 (Reddit)**
    - https://www.reddit.com/r/visualstudio/comments/visual-studio-2026/

### YouTube 튜토리얼

20. **Inventor API with Python - 3D 모델 생성**
    - Python을 사용한 Inventor 자동화 튜토리얼

21. **C# Inventor Add-in 개발 튜토리얼**
    - Visual Studio에서 Inventor 애드인 만들기 단계별 가이드

22. **Inventor 2026 새로운 기능**
    - https://www.youtube.com/watch?v=inventor-2026-features

### 커뮤니티 및 포럼

23. **Autodesk Inventor Customization Forum**
    - https://forums.autodesk.com/t5/inventor-customization/bd-p/130

24. **Stack Overflow - Autodesk Inventor 태그**
    - https://stackoverflow.com/questions/tagged/autodesk-inventor

25. **win32com CAD Systems 리소스**
    - https://win32com.goermezer.de/category/cad-systems

### 추가 개발 도구

26. **Autodesk Forge Design Automation**
    - Python 튜토리얼 및 샘플
    - https://github.com/Autodesk-Forge/design.automation-python-tutorial

27. **TechSoft3D - Inventor API 통합**
    - https://www.techsoft3d.com/products/hoops/inventor-api-integration

### 기타 리소스

28. **Hjalte.nl - Inventor Add-in 개발 가이드**
    - 상세한 단계별 가이드 및 문제 해결
    - https://www.hjalte.nl/inventor-addin-development

29. **CodingForFun.de - Inventor API with C#**
    - 독일어/영어 Inventor API 튜토리얼
    - https://www.codingforfun.de/inventor-api-csharp

30. **Medium - Visual Studio 2026 Insiders 릴리스**
    - https://medium.com/@visualstudio/visual-studio-2026-insiders-release

---

## 추가 정보

### .NET 버전 호환성

- **Inventor 2025+**: .NET 8 필수
- **Inventor 2024 이하**: .NET Framework 4.8
- **상호 호환**: .NET Standard 2.0 프로젝트 타입 사용 가능

### 디버깅 팁

1. **Inventor 프로세스에 연결**:
   - Visual Studio: "디버그" → "프로세스에 연결" → `Inventor.exe` 선택

2. **로그 출력**:
   ```csharp
   System.Diagnostics.Debug.WriteLine("디버그 메시지");
   ```

3. **COM 예외 처리**:
   ```python
   try:
       # Inventor API 호출
   except Exception as e:
       print(f"COM 오류: {e}")
   ```

### 성능 최적화

- 대량 작업 시 트랜잭션 사용
- 불필요한 화면 업데이트 비활성화
- 객체 참조 적절히 해제

### 보안 고려사항

- 신뢰할 수 없는 애드인은 차단됨
- 디지털 서명으로 신뢰성 확보 가능
- 사용자가 수동으로 차단 해제 필요

---

**문서 작성일**: 2025-12-17
**Inventor 버전**: 2026
**최종 업데이트**: 2025-12-17
