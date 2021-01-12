import Model from '@ember-data/model';

export default class BookModel extends Model {
  @attr('string') title;
  @attr('string') author;
  @attr('string') description;
}
