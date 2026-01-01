# CopyDesignFileInput.isCopyDrawings Property![](../images/TestTubeLarge.png)

Parent Object: [CopyDesignFileInput](CopyDesignFileInput.htm)

![Preview](../images/TestTubeSmall.png)This functionality is provided as a preview
of intended future API capabilities. You are encouraged to use it and report any problems or suggestions using the
[Fusion API and Scripts](https://forums.autodesk.com/t5/fusion-360-api-and-scripts/bd-p/22) forum.

Because this is a preview of future functionality, there is the possibility that it will change, which will possibly
break any existing programs that use this functionality. Because of that, you should never deliver any programs that use
any preview capabilities. For a distributed program, you should wait until it has moved from preview to released state.

Defined in namespace "adsk::core" and the header file is <Core/Dashboard/CopyDesignFileInput.h>

## Description

Gets and sets if any drawings associated with the design should also be copied.

## Syntax

* [Python](#Python)
* [C++](#C++)

"copyDesignFileInput\_var" is a variable referencing a CopyDesignFileInput object. |

"copyDesignFileInput\_var" is a variable referencing a CopyDesignFileInput object. ```` ``` #include <Core/Dashboard/CopyDesignFileInput.h>  // Get the value of the property. boolean propertyValue = copyDesignFileInput_var->isCopyDrawings();  // Set the value of the property, where value_var is a boolean. bool returnValue = copyDesignFileInput_var->isCopyDrawings(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version May 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |