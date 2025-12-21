# UserInputEvents.OnContextualMiniToolbar Event

Parent Object: [UserInputEvents](../UserInputEvents/UserInputEvents.md)

## Description

Fires before contextual commands are displayed to the user in the graphics window when the user selects an object.

## Syntax

UserInputEvents.**OnContextualMiniToolbar**( ***SelectedEntities*** As [ObjectsEnumerator](../ObjectsEnumerator/ObjectsEnumerator.md), ***DisplayedCommands*** As [NameValueMap](../NameValueMap/NameValueMap.md), ***AdditionalInfo*** As [NameValueMap](../NameValueMap/NameValueMap.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| SelectedEntities | [ObjectsEnumerator](../ObjectsEnumerator/ObjectsEnumerator.md) | Input ObjectsEnumerator that contains the selected entities. This is the same set of entities currently contained in the document’s SelectSet. |
| DisplayedCommands | [NameValueMap](../NameValueMap/NameValueMap.md) | Input NameValueMap object that contains the commands that should be displayed. Name contains the internal name of the command and Value contains the entity to be highlighted when the user hovers over this command in the contextual toolbar. |
| AdditionalInfo | [NameValueMap](../NameValueMap/NameValueMap.md) | Input NameValueMap object that contains additional information about why the menu is being displayed. This is currently empty. |

## Version

Introduced in version 2012
