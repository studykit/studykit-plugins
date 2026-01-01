# TransitionSymbolStyle Object

Derived from: [Style](../Style/Style.md) Object

## Description

TransitionSymbolStyle object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [ConvertToLocal](../TransitionSymbolStyle/TransitionSymbolStyle_ConvertToLocal.md) | Method that creates a local cached copy of a global style and returns the local style. |
| [Copy](../TransitionSymbolStyle/TransitionSymbolStyle_Copy.md) | Method that creates a new local Style object. The newly created style is returned. |
| [Delete](../TransitionSymbolStyle/TransitionSymbolStyle_Delete.md) | Method that deletes the Style/Layer/UnfoldMethod. |
| [GetReferenceKey](../TransitionSymbolStyle/TransitionSymbolStyle_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [SaveToGlobal](../TransitionSymbolStyle/TransitionSymbolStyle_SaveToGlobal.md) | Method that saves this style to the global repository. If a style with the same name is found in the repository, that style is updated. |
| [UpdateFromGlobal](../TransitionSymbolStyle/TransitionSymbolStyle_UpdateFromGlobal.md) | Method that updates this style from the global repository. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../TransitionSymbolStyle/TransitionSymbolStyle_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Comments](../TransitionSymbolStyle/TransitionSymbolStyle_Comments.md) | Gets and sets comments associated with the style. |
| [InternalName](../TransitionSymbolStyle/TransitionSymbolStyle_InternalName.md) | Property that returns the internal name of the style. The name is the internal English name of the standard style. This name will remain constant and is not affected by locale. This name is never displayed to the user. Note that this name is not guaranteed to be unique. |
| [InUse](../TransitionSymbolStyle/TransitionSymbolStyle_InUse.md) | Property that indicates if this style is in use. |
| [LeaderStyleForEdgeSelected](../TransitionSymbolStyle/TransitionSymbolStyle_LeaderStyleForEdgeSelected.md) | Gets and sets the leader style used for the transition symbol style when attaches to geometry. |
| [LeaderStyleForFaceSelected](../TransitionSymbolStyle/TransitionSymbolStyle_LeaderStyleForFaceSelected.md) | Gets and sets the leader style used for the transition symbol style when attaches to drawing view. |
| [Name](../TransitionSymbolStyle/TransitionSymbolStyle_Name.md) | Gets/Sets the name of the Style. |
| [Parent](../TransitionSymbolStyle/TransitionSymbolStyle_Parent.md) | Property returning the parent of this object. |
| [StyleLocation](../TransitionSymbolStyle/TransitionSymbolStyle_StyleLocation.md) | Property that returns the location of this style, i.e. local to the document, cached locally in the document, exists in the library. Styles that exist in the library cannot be edited. |
| [StyleType](../TransitionSymbolStyle/TransitionSymbolStyle_StyleType.md) | Gets the type of the style. |
| [TextStyle](../TransitionSymbolStyle/TransitionSymbolStyle_TextStyle.md) | Gets and sets the text style used for the transition symbol style. |
| [Type](../TransitionSymbolStyle/TransitionSymbolStyle_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [UpToDate](../TransitionSymbolStyle/TransitionSymbolStyle_UpToDate.md) | Property that gets the up-to-date status of the style against the global repository. |

## Accessed From

[ObjectDefaultsStyle.TransitionSymbolStyle](../ObjectDefaultsStyle/ObjectDefaultsStyle_TransitionSymbolStyle.md), [TransitionSymbolDefinition.Style](../TransitionSymbolDefinition/TransitionSymbolDefinition_Style.md), [TransitionSymbolStylesEnumerator.Item](../TransitionSymbolStylesEnumerator/TransitionSymbolStylesEnumerator_Item.md)

## Version

Introduced in version 2025.1
