# Viewport.setCurrentAsHome Method

Parent Object: [Viewport](Viewport.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/Viewport.h>

## Description

Sets the "home" view to be the current view orientation.

## Syntax

* [Python](#Python)
* [C++](#C++)

"viewport\_var" is a variable referencing a [Viewport](Viewport.htm) object.```` ``` returnValue = viewport_var.setCurrentAsHome(isFitToView) ``` ```` |

"viewport\_var" is a variable referencing a [Viewport](Viewport.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if setting the view orientation was successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| isFitToView | boolean | Specifies if when the view goes "home" if the view should be fit to the model or not. True indicates the view will be fit to the model. |

## Version

Introduced in version September 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |