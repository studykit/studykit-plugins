# DataHub.mfgdmId Property![](../images/TestTubeLarge.png)

Parent Object: [DataHub](DataHub.htm)

![Preview](../images/TestTubeSmall.png)This functionality is provided as a preview
of intended future API capabilities. You are encouraged to use it and report any problems or suggestions using the
[Fusion API and Scripts](https://forums.autodesk.com/t5/fusion-360-api-and-scripts/bd-p/22) forum.

Because this is a preview of future functionality, there is the possibility that it will change, which will possibly
break any existing programs that use this functionality. Because of that, you should never deliver any programs that use
any preview capabilities. For a distributed program, you should wait until it has moved from preview to released state.

Defined in namespace "adsk::core" and the header file is <Core/Dashboard/DataHub.h>

## Description

Get the MFGDM ID for this hub.

## Syntax

* [Python](#Python)
* [C++](#C++)

"dataHub\_var" is a variable referencing a DataHub object. |

"dataHub\_var" is a variable referencing a DataHub object. ```` ``` #include <Core/Dashboard/DataHub.h>  // Get the value of the property. string propertyValue = dataHub_var->mfgdmId(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version July 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |