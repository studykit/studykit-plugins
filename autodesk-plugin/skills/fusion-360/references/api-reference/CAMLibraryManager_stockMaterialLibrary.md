# CAMLibraryManager.stockMaterialLibrary Property![](../images/TestTubeLarge.png)

Parent Object: [CAMLibraryManager](CAMLibraryManager.htm)

![Preview](../images/TestTubeSmall.png)This functionality is provided as a preview
of intended future API capabilities. You are encouraged to use it and report any problems or suggestions using the
[Fusion API and Scripts](https://forums.autodesk.com/t5/fusion-360-api-and-scripts/bd-p/22) forum.

Because this is a preview of future functionality, there is the possibility that it will change, which will possibly
break any existing programs that use this functionality. Because of that, you should never deliver any programs that use
any preview capabilities. For a distributed program, you should wait until it has moved from preview to released state.

Defined in namespace "adsk::cam" and the header file is <Cam/Global/CAMLibraryManager.h>

## Description

The StockMaterialLibrary provides access to stock materials. You can only get a valid StockMaterialLibrary when you have access to Stock Materials private preview feature and enable the feature flag.

## Syntax

* [Python](#Python)
* [C++](#C++)

"cAMLibraryManager\_var" is a variable referencing a CAMLibraryManager object. |

"cAMLibraryManager\_var" is a variable referencing a CAMLibraryManager object. ```` ``` #include <Cam/Global/CAMLibraryManager.h>  // Get the value of the property. Ptr<StockMaterialLibrary> propertyValue = cAMLibraryManager_var->stockMaterialLibrary(); ``` ```` |

## Property Value

This is a read only property whose value is a [StockMaterialLibrary](StockMaterialLibrary.htm).

## Version

Introduced in version September 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |