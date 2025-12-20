# SheetMetalStyle Object

Derived from: [Style](../Style/Style.md) Object

## Description

The SheetMetalStyle object contains all of the information about a particular sheet metal style (these are also referred to as sheet metal rules).

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Activate](../SheetMetalStyle/SheetMetalStyle_Activate.md) | Method that causes this sheet metal style to become the active sheet metal style for this document. |
| [ConvertToLocal](../SheetMetalStyle/SheetMetalStyle_ConvertToLocal.md) | Method that creates a local cached copy of a global style and returns the local style. |
| [Copy](../SheetMetalStyle/SheetMetalStyle_Copy.md) | Method that creates a new local Style object. The newly created style is returned. |
| [Delete](../SheetMetalStyle/SheetMetalStyle_Delete.md) | Method that deletes the Style/Layer/UnfoldMethod. |
| [GetReferenceKey](../SheetMetalStyle/SheetMetalStyle_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [SaveToGlobal](../SheetMetalStyle/SheetMetalStyle_SaveToGlobal.md) | Method that saves this style to the global repository. If a style with the same name is found in the repository, that style is updated. |
| [UpdateFromGlobal](../SheetMetalStyle/SheetMetalStyle_UpdateFromGlobal.md) | Method that updates this style from the global repository. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../SheetMetalStyle/SheetMetalStyle_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [BendAngleReportType](../SheetMetalStyle/SheetMetalStyle_BendAngleReportType.md) | Gets and sets which angle is to be reported in the flat pattern. |
| [BendRadius](../SheetMetalStyle/SheetMetalStyle_BendRadius.md) | Gets and sets the expression that defines the value of the bend radius depth. |
| [BendReliefDepth](../SheetMetalStyle/SheetMetalStyle_BendReliefDepth.md) | Gets and sets the expression that defines the value of the bend relief depth. |
| [BendReliefShape](../SheetMetalStyle/SheetMetalStyle_BendReliefShape.md) | Gets/Sets BendReliefShape. |
| [BendReliefWidth](../SheetMetalStyle/SheetMetalStyle_BendReliefWidth.md) | Gets and sets the expression that defines the value of the bend relief width. |
| [BendTransition](../SheetMetalStyle/SheetMetalStyle_BendTransition.md) | Gets/Sets BendTransition. |
| [BendTransitionArcRadius](../SheetMetalStyle/SheetMetalStyle_BendTransitionArcRadius.md) | Gets and sets the expression that defines the value of the bend relief arc radius. |
| [Comments](../SheetMetalStyle/SheetMetalStyle_Comments.md) | Gets and sets comments associated with the style. |
| [CornerReliefPlacement](../SheetMetalStyle/SheetMetalStyle_CornerReliefPlacement.md) | Gets and sets corner relief placement (valid only for square and round corners). |
| [CornerReliefShape](../SheetMetalStyle/SheetMetalStyle_CornerReliefShape.md) | Gets and sets the expression that defines the value of the corner relief size radius. |
| [CornerReliefSize](../SheetMetalStyle/SheetMetalStyle_CornerReliefSize.md) | Gets CornerReliefSize. |
| [GapSize](../SheetMetalStyle/SheetMetalStyle_GapSize.md) | Gets and sets the expression that defines the value of the gap size for miters, seams, and rips. |
| [InternalName](../SheetMetalStyle/SheetMetalStyle_InternalName.md) | Property that returns the internal name of the style. The name is the internal English name of the standard style. This name will remain constant and is not affected by locale. This name is never displayed to the user. Note that this name is not guaranteed to be unique. |
| [InUse](../SheetMetalStyle/SheetMetalStyle_InUse.md) | Property that indicates if this style is in use. |
| [MinimumRemnant](../SheetMetalStyle/SheetMetalStyle_MinimumRemnant.md) | Gets and sets the expression that defines the value of the corner relief size radius. |
| [Name](../SheetMetalStyle/SheetMetalStyle_Name.md) | Gets/Sets the name of the Style. |
| [Parent](../SheetMetalStyle/SheetMetalStyle_Parent.md) | Property returning the parent of this object. |
| [PunchRepresentationType](../SheetMetalStyle/SheetMetalStyle_PunchRepresentationType.md) | Gets and sets the default punch representation type. |
| [StyleLocation](../SheetMetalStyle/SheetMetalStyle_StyleLocation.md) | Property that returns the location of this style, i.e. local to the document, cached locally in the document, exists in the library. Styles that exist in the library cannot be edited. |
| [StyleType](../SheetMetalStyle/SheetMetalStyle_StyleType.md) | Gets the type of the style. |
| [Thickness](../SheetMetalStyle/SheetMetalStyle_Thickness.md) | Read-write property that gets and sets the expression that defines the value of the thickness. |
| [ThreeBendCornerReliefShape](../SheetMetalStyle/SheetMetalStyle_ThreeBendCornerReliefShape.md) | Gets and sets the expression that defines the value of the corner relief size radius. |
| [ThreeBendCornerReliefSize](../SheetMetalStyle/SheetMetalStyle_ThreeBendCornerReliefSize.md) | Get the parameter that defines the three bend corner relief size for this style. |
| [Type](../SheetMetalStyle/SheetMetalStyle_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [UnfoldMethod](../SheetMetalStyle/SheetMetalStyle_UnfoldMethod.md) | Read-write property that gets and set the unfold method associated with the style. |
| [UpToDate](../SheetMetalStyle/SheetMetalStyle_UpToDate.md) | Property that gets the up-to-date status of the style against the global repository. |

## Accessed From

[ContourFlangeDefinition.SheetMetalRule](../ContourFlangeDefinition/ContourFlangeDefinition_SheetMetalRule.md), [FaceFeatureDefinition.SheetMetalRule](../FaceFeatureDefinition/FaceFeatureDefinition_SheetMetalRule.md), [LoftedFlangeDefinition.SheetMetalRule](../LoftedFlangeDefinition/LoftedFlangeDefinition_SheetMetalRule.md), [SheetMetalComponentDefinition.ActiveSheetMetalStyle](../SheetMetalComponentDefinition/SheetMetalComponentDefinition_ActiveSheetMetalStyle.md), [SheetMetalComponentDefinition.GetBodySheetMetalStyle](../SheetMetalComponentDefinition/SheetMetalComponentDefinition_GetBodySheetMetalStyle.md), [SheetMetalStyles.Item](../SheetMetalStyles/SheetMetalStyles_Item.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Sheet Metal Style Display](../../sample-programs/SheetMetalStyle_Sample.md) | This sample illustrates getting information about sheet metal styles. |
| [Sheet Metal Style Creation](../../sample-programs/SheetMetalStyles_Sample.md) | This sample illustrates creating a new sheet metal style. It uses a bend table and assumes the sample bend table delivered with Inventor is available. You can edit the path below to reference any existing bend table. To use the sample make sure a bend table is available at the specified path, open a sheet metal document, and run the sample. |

## Version

Introduced in version 5.3

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |