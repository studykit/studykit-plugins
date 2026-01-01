# DataComponent.component Property![](../images/TestTubeLarge.png)

Parent Object: [DataComponent](DataComponent.htm)

![Preview](../images/TestTubeSmall.png)This functionality is provided as a preview
of intended future API capabilities. You are encouraged to use it and report any problems or suggestions using the
[Fusion API and Scripts](https://forums.autodesk.com/t5/fusion-360-api-and-scripts/bd-p/22) forum.

Because this is a preview of future functionality, there is the possibility that it will change, which will possibly
break any existing programs that use this functionality. Because of that, you should never deliver any programs that use
any preview capabilities. For a distributed program, you should wait until it has moved from preview to released state.

Defined in namespace "adsk::core" and the header file is <Core/Dashboard/DataComponent.h>

## Description

Get the fusion.Component that corresponds to this data component.

## Syntax

* [Python](#Python)
* [C++](#C++)

"dataComponent\_var" is a variable referencing a DataComponent object. |

"dataComponent\_var" is a variable referencing a DataComponent object. ```` ``` #include <Core/Dashboard/DataComponent.h>  // Get the value of the property. Ptr<Base> propertyValue = dataComponent_var->component(); ``` ```` |

## Property Value

This is a read only property whose value is a [Base](Base.htm).

## Version

Introduced in version July 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |