# DataComponent.id Property![](../images/TestTubeLarge.png)

Parent Object: [DataComponent](DataComponent.htm)

![Preview](../images/TestTubeSmall.png)This functionality is provided as a preview
of intended future API capabilities. You are encouraged to use it and report any problems or suggestions using the
[Fusion API and Scripts](https://forums.autodesk.com/t5/fusion-360-api-and-scripts/bd-p/22) forum.

Because this is a preview of future functionality, there is the possibility that it will change, which will possibly
break any existing programs that use this functionality. Because of that, you should never deliver any programs that use
any preview capabilities. For a distributed program, you should wait until it has moved from preview to released state.

Defined in namespace "adsk::core" and the header file is <Core/Dashboard/DataComponent.h>

## Description

Gets the unique ID of this DataComponent. This ID can be used within the MFG DM API. This ID is created by the MFG DM API when the component is first saved.

## Syntax

* [Python](#Python)
* [C++](#C++)

"dataComponent\_var" is a variable referencing a DataComponent object. |

"dataComponent\_var" is a variable referencing a DataComponent object. ```` ``` #include <Core/Dashboard/DataComponent.h>  // Get the value of the property. string propertyValue = dataComponent_var->id(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version May 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |