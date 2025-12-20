# AnalysisManager Object

## Description

The AnalysisManager object provides access to all types of surface analysis in a part document.

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [ActiveAnalysis](../AnalysisManager/AnalysisManager_ActiveAnalysis.md) | Property that returns the active analysis object. |
| [ActiveAnalysisType](../AnalysisManager/AnalysisManager_ActiveAnalysisType.md) | Property that returns the enum indicating the type of the currently active analysis. |
| [Application](../AnalysisManager/AnalysisManager_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [DraftAnalyses](../AnalysisManager/AnalysisManager_DraftAnalyses.md) | Property that returns the DraftAnalyses collection object. |
| [IsAnalysisVisible](../AnalysisManager/AnalysisManager_IsAnalysisVisible.md) | Gets/Sets whether the analysis visibility is turned on. |
| [Parent](../AnalysisManager/AnalysisManager_Parent.md) | Property that returns the parent ComponentDefinition object. |
| [Type](../AnalysisManager/AnalysisManager_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[DraftAnalysis.Parent](../DraftAnalysis/DraftAnalysis_Parent.md), [PartComponentDefinition.AnalysisManager](../PartComponentDefinition/PartComponentDefinition_AnalysisManager.md), [SheetMetalComponentDefinition.AnalysisManager](../SheetMetalComponentDefinition/SheetMetalComponentDefinition_AnalysisManager.md)

## Version

Introduced in version 2009

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |