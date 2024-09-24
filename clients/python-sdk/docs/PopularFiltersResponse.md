# PopularFiltersResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**popular_filters** | [**List[PopularFilters]**](PopularFilters.md) |  | 

## Example

```python
from trieve_py_client.models.popular_filters_response import PopularFiltersResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PopularFiltersResponse from a JSON string
popular_filters_response_instance = PopularFiltersResponse.from_json(json)
# print the JSON string representation of the object
print(PopularFiltersResponse.to_json())

# convert the object into a dict
popular_filters_response_dict = popular_filters_response_instance.to_dict()
# create an instance of PopularFiltersResponse from a dict
popular_filters_response_form_dict = popular_filters_response.from_dict(popular_filters_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

