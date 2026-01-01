# CAM.postProcessAll Method

Parent Object: [CAM](CAM.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/CAM/CAM.h>

## Description

This function is retired. See more information in the 'Remarks' section below.

## Syntax

* [Python](#Python)
* [C++](#C++)

"cAM\_var" is a variable referencing a [CAM](CAM.htm) object.```` ``` returnValue = cAM_var.postProcessAll(input) ``` ```` |

"cAM\_var" is a variable referencing a [CAM](CAM.htm) object.  ```` ``` #include <Cam/CAM/CAM.h>  returnValue = cAM_var->postProcessAll(input); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| input | [PostProcessInput](PostProcessInput.htm) | The PostProcessInput object that defines the post options and parameters. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Post Toolpaths API Sample](PostToolpaths_Sample_Sample.htm) | Demonstrates posting toolpaths in the active document. |

## Version

Introduced in version January 2016
Retired in version September 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |