# UnfoldMethod Object

Derived from: [Style](../Style/Style.md) Object

## Description

The UnfoldMethod object provides access to the information associated with a specific unfold method. This object derives from the Style object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [ConvertToLocal](../UnfoldMethod/UnfoldMethod_ConvertToLocal.md) | Method that creates a local cached copy of a global style and returns the local style. |
| [Copy](../UnfoldMethod/UnfoldMethod_Copy.md) | Method that creates a new local Style object. The newly created style is returned. |
| [Delete](../UnfoldMethod/UnfoldMethod_Delete.md) | Method that deletes the Style/Layer/UnfoldMethod. |
| [DeleteEquation](../UnfoldMethod/UnfoldMethod_DeleteEquation.md) | Method that deletes the specified equation. An equation unfold method always needs to have at least one equation. Deleting the last equation will cause a default equation to be created. |
| [GetEquation](../UnfoldMethod/UnfoldMethod_GetEquation.md) | Method that sets this unfold method to be an equation type of unfold method and defines the associated equation and limits. |
| [GetReferenceKey](../UnfoldMethod/UnfoldMethod_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [SaveToGlobal](../UnfoldMethod/UnfoldMethod_SaveToGlobal.md) | Method that saves this style to the global repository. If a style with the same name is found in the repository, that style is updated. |
| [SetEquation](../UnfoldMethod/UnfoldMethod_SetEquation.md) | Method that creates or edits an equation associated with this unfold method. Creating the first equation will change the unfold method be to a custom equation type of unfold method. |
| [UpdateFromGlobal](../UnfoldMethod/UnfoldMethod_UpdateFromGlobal.md) | Method that updates this style from the global repository. |
| [WriteBendTableToFile](../UnfoldMethod/UnfoldMethod_WriteBendTableToFile.md) | Method that writes the bend table information of the UnfoldMethod object into an external file. This method is only valid in the case where UnfoldMethodType is kBendTableUnfoldMethod. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../UnfoldMethod/UnfoldMethod_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [BendAngleType](../UnfoldMethod/UnfoldMethod_BendAngleType.md) | Gets and sets whether the bend or open angle value is to be used for the angle in equations. |
| [Comments](../UnfoldMethod/UnfoldMethod_Comments.md) | Gets and sets comments associated with the style. |
| [EquationCount](../UnfoldMethod/UnfoldMethod_EquationCount.md) | Property that reports the number of equations currently associated with this unfold method. This property is only used in the case where the UnfoldMethodType property returns kCustomEquationUnfoldMethod and will return 0 for other unfold method types. |
| [EquationType](../UnfoldMethod/UnfoldMethod_EquationType.md) | Property that specifies the type of equation defined for the unfold method. This property is only valid in the case where the UnfoldMethodType property returns kCustomEquationUnfoldMethod. In all other cases the value of this property should be ignored. |
| [InternalName](../UnfoldMethod/UnfoldMethod_InternalName.md) | Property that returns the internal name of the style. The name is the internal English name of the standard style. This name will remain constant and is not affected by locale. This name is never displayed to the user. Note that this name is not guaranteed to be unique. |
| [InUse](../UnfoldMethod/UnfoldMethod_InUse.md) | Property that indicates if this style is in use. |
| [kFactor](../UnfoldMethod/UnfoldMethod_kFactor.md) | Gets/sets the kFactor associated with this unfold method. |
| [Name](../UnfoldMethod/UnfoldMethod_Name.md) | Gets/Sets the name of the Style. |
| [Parent](../UnfoldMethod/UnfoldMethod_Parent.md) | Property returning the parent of this object. |
| [SplineFactor](../UnfoldMethod/UnfoldMethod_SplineFactor.md) | Gets and sets the factor used when unfolding ruled surfaces defined using ellipses and splines. |
| [StyleLocation](../UnfoldMethod/UnfoldMethod_StyleLocation.md) | Property that returns the location of this style, i.e. local to the document, cached locally in the document, exists in the library. Styles that exist in the library cannot be edited. |
| [StyleType](../UnfoldMethod/UnfoldMethod_StyleType.md) | Gets the type of the style. |
| [Type](../UnfoldMethod/UnfoldMethod_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [UnfoldMethodType](../UnfoldMethod/UnfoldMethod_UnfoldMethodType.md) | Property that returns the type of unfold method used by this UnfoldMethod object. kLinearUnfoldMethod, kBendTableUnfoldMethod, and kCustomEquationUnfoldMethod are possible return values. |
| [UpToDate](../UnfoldMethod/UnfoldMethod_UpToDate.md) | Property that gets the up-to-date status of the style against the global repository. |

## Accessed From

[BendDefinition.UnfoldMethod](../BendDefinition/BendDefinition_UnfoldMethod.md), [ContourFlangeDefinition.UnfoldMethod](../ContourFlangeDefinition/ContourFlangeDefinition_UnfoldMethod.md), [FlangeDefinition.UnfoldMethod](../FlangeDefinition/FlangeDefinition_UnfoldMethod.md), [FoldDefinition.UnfoldMethod](../FoldDefinition/FoldDefinition_UnfoldMethod.md), [HemDefinition.UnfoldMethod](../HemDefinition/HemDefinition_UnfoldMethod.md), [LoftedFlangeDefinition.UnfoldMethod](../LoftedFlangeDefinition/LoftedFlangeDefinition_UnfoldMethod.md), [SheetMetalComponentDefinition.UnfoldMethod](../SheetMetalComponentDefinition/SheetMetalComponentDefinition_UnfoldMethod.md), [SheetMetalStyle.UnfoldMethod](../SheetMetalStyle/SheetMetalStyle_UnfoldMethod.md), [UnfoldMethods.AddBendTableFromFile](../UnfoldMethods/UnfoldMethods_AddBendTableFromFile.md), [UnfoldMethods.AddEquationUnfoldMethod](../UnfoldMethods/UnfoldMethods_AddEquationUnfoldMethod.md), [UnfoldMethods.AddLinearUnfoldMethod](../UnfoldMethods/UnfoldMethods_AddLinearUnfoldMethod.md), [UnfoldMethods.Item](../UnfoldMethods/UnfoldMethods_Item.md)

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