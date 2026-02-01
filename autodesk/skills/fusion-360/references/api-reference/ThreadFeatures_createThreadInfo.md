# ThreadFeatures.createThreadInfo Method

Parent Object: [ThreadFeatures](ThreadFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ThreadFeatures.h>

## Description

This function is retired. See more information in the 'Remarks' section below.

## Remarks

This method has been replaced by the ThreadInfo.create method.

## Syntax

* [Python](#Python)
* [C++](#C++)

"threadFeatures\_var" is a variable referencing a [ThreadFeatures](ThreadFeatures.htm) object.```` ``` returnValue = threadFeatures_var.createThreadInfo(isInternal, threadType, threadDesignation, threadClass) ``` ```` |

"threadFeatures\_var" is a variable referencing a [ThreadFeatures](ThreadFeatures.htm) object.  ```` ``` #include <Fusion/Features/ThreadFeatures.h>  returnValue = threadFeatures_var->createThreadInfo(isInternal, threadType, threadDesignation, threadClass); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ThreadInfo](ThreadInfo.htm) | Returns the newly created ThreadInfo object or null if the creation failed. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| isInternal | boolean | Input Boolean that indicates if the thread is an internal or external thread. A value of true indicates an internal thread. |
| threadType | string | Input string that defines the thread type. |
| threadDesignation | string | Input string that contains the thread designation. This is input as the full thread designation that will be used in a drawing for the thread call-out. The nominal size and pitch information are extracted from the designation. |
| threadClass | string | Input string that defines the thread class. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Thread Feature API Sample](ThreadFeatureSample_Sample.htm) | Demonstrates creating a new thread feature. |

## Version

Introduced in version January 2015
Retired in version September 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |