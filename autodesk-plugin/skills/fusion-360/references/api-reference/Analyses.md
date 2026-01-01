# Analyses Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/Analyses.h>

## Description

Provides access to the existing analysis results within a design.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](Analyses_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [item](Analyses_item.htm) | A method that returns the specified Analysis using an index into the collection. |
| [itemByName](Analyses_itemByName.htm) | A method that returns the specified Analysis using the name of the analysis as it is displayed in the browser. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [accessibilityAnalyses](Analyses_accessibilityAnalyses.htm) | Returns the AccessibilityAnalyses object, which provides access to any existing AccessibilityAnalysis objects in the design. |
| [count](Analyses_count.htm) | Returns the number of Analysis objects in the collection. |
| [curvatureCombAnalyses](Analyses_curvatureCombAnalyses.htm) | Returns the CurvatureCombAnalyses object, which provides access to any existing CurvatureCombAnalysis objects in the design. |
| [curvatureMapAnalyses](Analyses_curvatureMapAnalyses.htm) | Returns the CurvatureMapAnalyses object, which provides access to any existing CurvatureMapAnalysis objects in the design. |
| [draftAnalyses](Analyses_draftAnalyses.htm) | Returns the DraftAnalyses object, which provides access to any existing DraftAnalysis objects in the design. |
| [isLightBulbOn](Analyses_isLightBulbOn.htm) | A property that gets and sets if the display is enabled for all Analysis objects in the design. If this is false, all Analysis results will be hidden. If this is true, the Analysis objects whose isLightBulbOn property is also true will be visible. |
| [isoCurveAnalyses](Analyses_isoCurveAnalyses.htm) | Returns the IsoCurveAnalyses object, which provides access to any existing IsoCurveAnalysis objects in the design. |
| [isValid](Analyses_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [minimumRadiusAnalyses](Analyses_minimumRadiusAnalyses.htm) | Returns the MinimumRadiusAnalyses object, which provides access to any existing MinimumRadiusAnalysis objects in the design. |
| [objectType](Analyses_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [sectionAnalyses](Analyses_sectionAnalyses.htm) | Returns the SectionAnalyses object, which provides access to any existing SectionAnalysis objects in the design. |
| [zebraAnalyses](Analyses_zebraAnalyses.htm) | Returns the ZebraAnalyses object, which provides access to any existing ZebraAnalysis objects in the design. |

## Accessed From

[Design.analyses](Design_analyses.htm), [FlatPatternProduct.analyses](FlatPatternProduct_analyses.htm), [WorkingModel.analyses](WorkingModel_analyses.htm)

## Version

Introduced in version January 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |