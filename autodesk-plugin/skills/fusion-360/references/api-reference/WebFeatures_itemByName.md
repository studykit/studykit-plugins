# WebFeatures.itemByName Method

Parent Object: [WebFeatures](WebFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/WebFeatures.h>

## Description

Function that returns the specified web feature using the name of the feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"webFeatures\_var" is a variable referencing a [WebFeatures](WebFeatures.htm) object.```` ``` returnValue = webFeatures_var.itemByName(name) ``` ```` |

"webFeatures\_var" is a variable referencing a [WebFeatures](WebFeatures.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [WebFeature](WebFeature.htm) | Returns the specified item or null if the specified name was not found. |

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