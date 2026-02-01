# TrimFeatureInput.cancel Method

Parent Object: [TrimFeatureInput](TrimFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/TrimFeatureInput.h>

## Description

To determine the possible boundaries and allow you to choose which cells to keep, the trim feature does a partial compute when the input object is created. To do this it starts a trim feature transaction and completes the transaction when you call the add method. If you don't call the add method it leaves Fusion in a bad state and there will be undo problems and it will possibly crash. If you have created a TrimFeatureInput object and don't want to finish the feature creation, you need to call the cancel method on the TrimFeatureInput object to safely abort the current trim feature transaction.

## Syntax

* [Python](#Python)
* [C++](#C++)

"trimFeatureInput\_var" is a variable referencing a [TrimFeatureInput](TrimFeatureInput.htm) object.```` ``` returnValue = trimFeatureInput_var.cancel() ``` ```` |

"trimFeatureInput\_var" is a variable referencing a [TrimFeatureInput](TrimFeatureInput.htm) object. |

## Version

Introduced in version April 2019

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |