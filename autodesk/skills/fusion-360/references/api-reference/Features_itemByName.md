# Features.itemByName Method

Parent Object: [Features](Features.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/Features.h>

## Description

Function that returns the specified feature using the name of the feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"features\_var" is a variable referencing a [Features](Features.htm) object.```` ``` returnValue = features_var.itemByName(name) ``` ```` |

"features\_var" is a variable referencing a [Features](Features.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [Feature](Feature.htm) | Returns the specified item or null if a feature matching the name was not found. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| name | string | The name of the feature within the collection to return. This is the same name seen in the timeline. |

## Version

Introduced in version September 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |