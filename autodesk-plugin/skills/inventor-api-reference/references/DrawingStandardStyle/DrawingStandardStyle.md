# DrawingStandardStyle Object

Derived from: [Style](../Style/Style.md) Object

## Description

The DrawingStandardStyle object represents a drawing standard.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [ConvertToLocal](../DrawingStandardStyle/DrawingStandardStyle_ConvertToLocal.md) | Method that creates a local cached copy of a global style and returns the local style. |
| [Copy](../DrawingStandardStyle/DrawingStandardStyle_Copy.md) | Method that creates a new local Style object. The newly created style is returned. |
| [Delete](../DrawingStandardStyle/DrawingStandardStyle_Delete.md) | Method that deletes the Style/Layer/UnfoldMethod. |
| [GetAvailableStyles](../DrawingStandardStyle/DrawingStandardStyle_GetAvailableStyles.md) | Method that returns the ObjectCollection containing the styles which are available for the standard style. |
| [GetReferenceKey](../DrawingStandardStyle/DrawingStandardStyle_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [GetViewAnnotationDefaults](../DrawingStandardStyle/DrawingStandardStyle_GetViewAnnotationDefaults.md) | Method that gets the drawing view annotation defaults for the specified view type. |
| [GetViewLabelDefaults](../DrawingStandardStyle/DrawingStandardStyle_GetViewLabelDefaults.md) | Method that returns the drawing view label defaults for the specified view type. |
| [SaveToGlobal](../DrawingStandardStyle/DrawingStandardStyle_SaveToGlobal.md) | Method that saves this style to the global repository. If a style with the same name is found in the repository, that style is updated. |
| [SetAvailableStyles](../DrawingStandardStyle/DrawingStandardStyle_SetAvailableStyles.md) | Method that sets the styles which are available for the standard style. |
| [SetViewAnnotationDefaults](../DrawingStandardStyle/DrawingStandardStyle_SetViewAnnotationDefaults.md) | Method that sets the drawing view annotation defaults for the specified view type. |
| [SetViewLabelDefaults](../DrawingStandardStyle/DrawingStandardStyle_SetViewLabelDefaults.md) | Method that sets the drawing view label defaults for the specified view type. |
| [UpdateFromGlobal](../DrawingStandardStyle/DrawingStandardStyle_UpdateFromGlobal.md) | Method that updates this style from the global repository. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [ActiveObjectDefaults](../DrawingStandardStyle/DrawingStandardStyle_ActiveObjectDefaults.md) | Returns the active ObjectDefaultsStyle object. |
| [Application](../DrawingStandardStyle/DrawingStandardStyle_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [ApplyExcludeCharactersToBendTables](../DrawingStandardStyle/DrawingStandardStyle_ApplyExcludeCharactersToBendTables.md) | Gets and sets whether to exclude characters specified in the ExcludeCharacters property from bend tables and its associated tags. |
| [ApplyExcludeCharactersToHoleTables](../DrawingStandardStyle/DrawingStandardStyle_ApplyExcludeCharactersToHoleTables.md) | Gets and sets whether to exclude characters specified in the ExcludeCharacters property from hole tables and its associated tags. |
| [ApplyExcludeCharactersToRevisionTables](../DrawingStandardStyle/DrawingStandardStyle_ApplyExcludeCharactersToRevisionTables.md) | Gets and sets whether to exclude characters specified in the ExcludeCharacters property from revision tables and its associated tags. |
| [ApplyExcludeCharactersToViewNames](../DrawingStandardStyle/DrawingStandardStyle_ApplyExcludeCharactersToViewNames.md) | Gets and sets whether to exclude characters specified in the ExcludeCharacters property from view names. |
| [Comments](../DrawingStandardStyle/DrawingStandardStyle_Comments.md) | Gets and sets comments associated with the style. |
| [DecimalMarkerType](../DrawingStandardStyle/DrawingStandardStyle_DecimalMarkerType.md) | Gets and sets the character to use as a decimal marker. |
| [ExcludeCharacters](../DrawingStandardStyle/DrawingStandardStyle_ExcludeCharacters.md) | Gets and sets comma separated list of characters to be excluded from automatic alphabetical indexing. |
| [FirstAngleProjection](../DrawingStandardStyle/DrawingStandardStyle_FirstAngleProjection.md) | Gets and sets whether the projection type is first angle or third angle projection. |
| [FrontViewPlane](../DrawingStandardStyle/DrawingStandardStyle_FrontViewPlane.md) | Gets and sets the viewing plane to use as front view when creating a drawing view. |
| [GlobalLineScale](../DrawingStandardStyle/DrawingStandardStyle_GlobalLineScale.md) | Gets and sets the line scale for all line styles in the drawing. |
| [InternalName](../DrawingStandardStyle/DrawingStandardStyle_InternalName.md) | Property that returns the internal name of the style. The name is the internal English name of the standard style. This name will remain constant and is not affected by locale. This name is never displayed to the user. Note that this name is not guaranteed to be unique. |
| [InternationalStandardReference](../DrawingStandardStyle/DrawingStandardStyle_InternationalStandardReference.md) | Property that returns the International Standard on which this standard style is based. |
| [InUse](../DrawingStandardStyle/DrawingStandardStyle_InUse.md) | Property that indicates if this style is in use. |
| [LinearUnits](../DrawingStandardStyle/DrawingStandardStyle_LinearUnits.md) | Gets and sets the units of length measure. |
| [Name](../DrawingStandardStyle/DrawingStandardStyle_Name.md) | Gets/Sets the name of the Style. |
| [Parent](../DrawingStandardStyle/DrawingStandardStyle_Parent.md) | Property returning the parent of this object. |
| [PartialCircularThreadEdge](../DrawingStandardStyle/DrawingStandardStyle_PartialCircularThreadEdge.md) | Gets and sets thread edge display type for top views. |
| [PartialSectionThreadEnd](../DrawingStandardStyle/DrawingStandardStyle_PartialSectionThreadEnd.md) | Gets and sets thread edge display type for sectional views. |
| [PresetLineWeights](../DrawingStandardStyle/DrawingStandardStyle_PresetLineWeights.md) | Gets and sets an array of Doubles that specify the set of default values for line weights. |
| [PresetScales](../DrawingStandardStyle/DrawingStandardStyle_PresetScales.md) | Gets and sets an array of Strings that specify the set of default values for drawing view scales. |
| [PresetSectionHatchAngles](../DrawingStandardStyle/DrawingStandardStyle_PresetSectionHatchAngles.md) | Gets and sets an array of Doubles that specify the set of default values for section view hatch angles. |
| [PresetTextHeights](../DrawingStandardStyle/DrawingStandardStyle_PresetTextHeights.md) | Gets and sets an array of Doubles that specify the set of default values for text heights. |
| [StyleLocation](../DrawingStandardStyle/DrawingStandardStyle_StyleLocation.md) | Property that returns the location of this style, i.e. local to the document, cached locally in the document, exists in the library. Styles that exist in the library cannot be edited. |
| [StyleType](../DrawingStandardStyle/DrawingStandardStyle_StyleType.md) | Gets the type of the style. |
| [Type](../DrawingStandardStyle/DrawingStandardStyle_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [UpToDate](../DrawingStandardStyle/DrawingStandardStyle_UpToDate.md) | Property that gets the up-to-date status of the style against the global repository. |

## Accessed From

[DrawingStandardStylesEnumerator.Item](../DrawingStandardStylesEnumerator/DrawingStandardStylesEnumerator_Item.md), [DrawingStylesManager.ActiveStandardStyle](../DrawingStylesManager/DrawingStylesManager_ActiveStandardStyle.md)

## Version

Introduced in version 9
