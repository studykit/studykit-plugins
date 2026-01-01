# ThreadFeatures.threadDataQuery Property

Parent Object: [ThreadFeatures](ThreadFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ThreadFeatures.h>

## Description

This function is retired. See more information in the 'Remarks' section below.

## Remarks

This method has been replaced by the ThreadDataQuery.create method.

## Syntax

* [Python](#Python)
* [C++](#C++)

"threadFeatures\_var" is a variable referencing a ThreadFeatures object.  ```` ``` # Get the value of the property. propertyValue = threadFeatures_var.threadDataQuery ``` ```` |

"threadFeatures\_var" is a variable referencing a ThreadFeatures object. ```` ``` #include <Fusion/Features/ThreadFeatures.h>  // Get the value of the property. Ptr<ThreadDataQuery> propertyValue = threadFeatures_var->threadDataQuery(); ``` ```` |

## Property Value

This is a read only property whose value is a [ThreadDataQuery](ThreadDataQuery.htm).

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