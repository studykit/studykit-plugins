# ShellFeatures.itemByName Method

Parent Object: [ShellFeatures](ShellFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ShellFeatures.h>

## Description

Function that returns the specified shell feature using the name of the feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"shellFeatures\_var" is a variable referencing a [ShellFeatures](ShellFeatures.htm) object.```` ``` returnValue = shellFeatures_var.itemByName(name) ``` ```` |

"shellFeatures\_var" is a variable referencing a [ShellFeatures](ShellFeatures.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ShellFeature](ShellFeature.htm) | Returns the specified item or null if the specified name was not found. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| name | string | The name of the feature within the collection to return. This is the name seen in the timeline. |

## Version

Introduced in version September 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |