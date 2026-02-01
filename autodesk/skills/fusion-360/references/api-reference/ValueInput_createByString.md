# ValueInput.createByString Method

Parent Object: [ValueInput](ValueInput.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/ValueInput.h>

## Description

When a string is used to create a value it needs to be evaluated as an expression so its value can be determined using the UnitsManager class. The units of an expression can be explicitly defined or will default to the current default units. For example, if you create an expression with the string "6" and specify it as a length, it will use the current active units. If the current active units are defined as inches the expression will be interpreted as 6 inches. You can specify the units as part of the string (i.e. "6 mm"). You can also use equations in the string (i.e. "6 + 5mm")

## Syntax

* [Python](#Python)
* [C++](#C++)

This is a static method. ```` ```  returnValue = adsk.core.ValueInput.createByString(stringValue) ``` ```` |

This is a static method. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ValueInput](ValueInput.htm) | Returns the newly created ValueInput object or null if the creation failed. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| stringValue | string | The expression string |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Patch Feature API Sample](PatchFeatureSample_Sample.htm) | Demonstrates creating a new patch feature. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |