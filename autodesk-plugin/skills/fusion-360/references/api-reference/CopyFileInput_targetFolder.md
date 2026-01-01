# CopyFileInput.targetFolder Property![](../images/TestTubeLarge.png)

Parent Object: [CopyFileInput](CopyFileInput.htm)

![Preview](../images/TestTubeSmall.png)This functionality is provided as a preview
of intended future API capabilities. You are encouraged to use it and report any problems or suggestions using the
[Fusion API and Scripts](https://forums.autodesk.com/t5/fusion-360-api-and-scripts/bd-p/22) forum.

Because this is a preview of future functionality, there is the possibility that it will change, which will possibly
break any existing programs that use this functionality. Because of that, you should never deliver any programs that use
any preview capabilities. For a distributed program, you should wait until it has moved from preview to released state.

Defined in namespace "adsk::core" and the header file is <Core/Dashboard/CopyFileInput.h>

## Description

Gets and sets the target DataFolder where the design will be copied to.

## Syntax

* [Python](#Python)
* [C++](#C++)

"copyFileInput\_var" is a variable referencing a CopyFileInput object. |

"copyFileInput\_var" is a variable referencing a CopyFileInput object. ```` ``` #include <Core/Dashboard/CopyFileInput.h>  // Get the value of the property. Ptr<DataFolder> propertyValue = copyFileInput_var->targetFolder(); ``` ```` |

## Property Value

This is a read only property whose value is a [DataFolder](DataFolder.htm).

## Version

Introduced in version October 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |