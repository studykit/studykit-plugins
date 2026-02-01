# ThreadInfo.redefine Method

Parent Object: [ThreadInfo](ThreadInfo.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ThreadInfo.h>

## Description

Method that redefines an existing ThreadInfo object. This is typically used to change the thread of an existing thread or tapped hole.

## Syntax

* [Python](#Python)
* [C++](#C++)

"threadInfo\_var" is a variable referencing a [ThreadInfo](ThreadInfo.htm) object.```` ``` returnValue = threadInfo_var.redefine(isTapered, isInternal, threadType, threadDesignation, threadClass, isRightHanded) ``` ```` |

"threadInfo\_var" is a variable referencing a [ThreadInfo](ThreadInfo.htm) object.  ```` ``` #include <Fusion/Features/ThreadInfo.h>  returnValue = threadInfo_var->redefine(isTapered, isInternal, threadType, threadDesignation, threadClass, isRightHanded); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the redefinition was successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| isTapered | boolean | Input Boolean that indicates if the thread is straight or tapered. |
| isInternal | boolean | Input Boolean that indicates if the thread is internal or external. A value of true indicates an internal thread. This value is ignored when the ThreadInfo is used for a tapped hole since they are always internal. |
| threadType | string | Input string that defines the thread type. |
| threadDesignation | string | Input string that defines the thread designation. |
| threadClass | string | Input string that defines the thread class. This argument is ignored for tapered threads. |
| isRightHanded | boolean | Input Boolean that specifies if the thread is straight or tapered. |

## Version

Introduced in version September 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |