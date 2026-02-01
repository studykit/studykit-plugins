# ThreadFeature.setThreadOffsetLength Method

Parent Object: [ThreadFeature](ThreadFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ThreadFeature.h>

## Description

Sets the thread offset, length and location. Calling this method will cause the isFullLength property to be set to false.

## Syntax

* [Python](#Python)
* [C++](#C++)

"threadFeature\_var" is a variable referencing a [ThreadFeature](ThreadFeature.htm) object.```` ``` returnValue = threadFeature_var.setThreadOffsetLength(threadOffset, threadLength, threadLocation) ``` ```` |

"threadFeature\_var" is a variable referencing a [ThreadFeature](ThreadFeature.htm) object.  ```` ``` #include <Fusion/Features/ThreadFeature.h>  returnValue = threadFeature_var->setThreadOffsetLength(threadOffset, threadLength, threadLocation); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| threadOffset | [ValueInput](ValueInput.htm) | A ValueInput object that defines the thread offset. |
| threadLength | [ValueInput](ValueInput.htm) | A ValueInput object that defines the thread length. |
| threadLocation | [ThreadLocations](ThreadLocations.htm) | Indicates where the thread length is measured from. |

## Version

Introduced in version January 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |